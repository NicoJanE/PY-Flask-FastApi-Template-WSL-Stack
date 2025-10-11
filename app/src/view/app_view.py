"""
View layer for the Flask application.

This module handles the presentation logic and template rendering.
Views are responsible for preparing data and rendering HTML templates
in response to route handler requests.

"""

from flask import render_template
from logic.services_redis import analytics
import socket


class AppView:
    """
    Handles presentation logic and template rendering.
    
    This class acts as the View layer in the application architecture,
    responsible for:
    - Preparing data for template rendering
    - Calling Flask's render_template function
    - Coordinating with business logic services
    
    Naming Convention:
    - View methods use 'vw_' prefix (e.g., vw_login)
    - Corresponding route methods use 'rt_' prefix (e.g., rt_login)
    - This creates a clear mapping between routes and views
    
    """
    
    
    def __init__(self):
        """
        Initialize the AppView with required services.        
        - Sets up analytics service for tracking application metrics.
        
        """
        
        self.analytics_service = analytics.AnalyticsService()


    def vw_login(self, hostname, yourName):
        """
        Render the login/home page template.
        - Coordinates with analytics service to get hit count and renders the index.html template with the provided data.
        
        Args:
            hostname (str): Server hostname to display
            yourName (str): User name or identifier to display
            
        Returns:
            str: Rendered HTML content from index.html template
            
        """
        
        count_general = self.analytics_service.get_hit_count()
        count_user = self.analytics_service.get_hit_count(yourName)
        return render_template('index.html', hostname=hostname, count_general=count_general, count_user=count_user,yourName=yourName)
    
    
    # Redis 
    # SET Key value
    # SET age 25  
    # GET age   # always string
    # DEL age
    # EXISTS age
    # KEYS * # get all
    # flushall  # Removes everything
    ##
    ## Expiration
    # ttl name # displays howlong it will life, default -1 means for ever, -2 means it's gone
    # ttl name 10 # expires after 10 seconds
    # setex name2 10 nico   # name2 lives for 10 seconds
    #
    ## LIST
    # lpush friends anna
    # lpush friends nico
    # rpush friends mister  # added to end of list
    # get friends # fails needs:
    # lrange friends 0 -2  # Start index 1 stop at end (-1)
    # lpop  remove 1e left item
    # rpop  remove 1e right item
    #
    #
    # SETS  # unique list
    # SADD friends "Anna hartig"
    # SADD friends "Nico hart"
    # SADD friends "Nico hart"      # returns 0 cause is already available
    # SMEMBERS friends
    # SREM firends "Nico hart"      # remove items
    
    
    ## HASh key value pair inside key/value pair
    # HSET person name piet
    # HGET Person name
    # HEGT ALL person # prints: "name", "piet"
    # HSEt person age 54
    # HEGT ALL person # prints: "name", "piet". "54"
    # HEGT person name # prints: "piet". 
    # HEGT person age  # prints: "54"
    # HDEK person age   # delete
    # HEXISTS person name  #does name exists (1 yes 0 no)
    