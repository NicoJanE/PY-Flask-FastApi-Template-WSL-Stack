import os
import time
import redis
import socket

# Imported the needed Flask modules
from flask import Flask, render_template, request, redirect, url_for

# Get the directories where the script is located and the sub directories
app_dir = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, 
           template_folder=os.path.join(app_dir, 'templates'),
           static_folder=os.path.join(app_dir, 'static'))

# Redis configuration - use localhost for local development, 'redis' for Docker
redis_host = 'localhost' if os.getenv('FLASK_ENV') != 'development' else 'redis'
cache = redis.Redis(host=redis_host, port=6379)


def get_hit_count():
    retries = 5
    while True:
        try:
             return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                print(f"Redis connection failed: {exc}")
                return "Redis Error"
            retries -= 1
            time.sleep(0.5)
        except Exception as exc:
            print(f"Unexpected error in get_hit_count: {exc}")
            return "Error"

#Excute this when root page is openend
@app.route("/")
def index():
    count = get_hit_count()
    hostname = socket.gethostname()
    return render_template('index.html', hostname=hostname, count=count)


#Excute this when login page  is opened(currently vi root forms)
@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return render_template('index.html', yourName=user, count=get_hit_count())        
    else:
        user = ""
        user_name = request.args.get('nm')
        if user_name is None:
            user_name = ""
        user = user_name + "(None POST)"        
        return render_template('index.html', yourName=user, count=get_hit_count())


# Main setup
if __name__ == "__main__":
    # Simple profiling option
    if os.getenv('FLASK_PROFILE') == 'true':
        import cProfile
        import atexit
        
        pr = cProfile.Profile()
        pr.enable()
        
        def save_profile():
            pr.disable()
            pr.dump_stats('profile_output.prof')
            print("Profile saved to profile_output.prof")
        
        atexit.register(save_profile)
        print("Profiling enabled - profile will be saved on exit")
    
    app.run(host="0.0.0.0", port=8080, debug=False, use_reloader=False)


 # Reload true in debug mode, monitors file in source(including sub direcoties) and reload the server
                                                            # so that changes are direct viewable for a developer without need to restart server manually (python concept feature)
                                                            # TURN OFF in Production.
# use_reloader=true may have the effect that application runs twice, once with the debugger setting and once without, also it
# has the result that one has to stop the debugger action twice. This is super annoying, so we turn it off here. 
# No Idea what the option true brings to the table beside this annoyance. (not handy for debugging)
