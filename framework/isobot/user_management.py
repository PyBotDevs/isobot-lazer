"""The library used for managing user data in isobot."""

# Imports
import json
import time

# Classes
class UserManager():
    def __init__(self, db_path:str):
        self.db_path = db_path
        with open(self.db_path, 'r') as f:
            global userdat
            userdat = json.load(f)
    
    def save(self):
        """Saves databases cached on memory. (Using as standalone will force-dump all data)"""
        with open(self.db_path, 'w+') as f: json.dump(userdat, f, indent=4)
    
    def add_user(self, id:int):
        """Adds a new user to the user repository."""
        exctime = time.time()
        if str(id) not in userdat: 
            userdat[str(id)] = {"registered": exctime, "commands_run": 0, "job": None}
            save()
        else: return "That user ID is already registered!"

    def set_job(self, user:int, jobname:str):
        """Sets a job for a user."""
        try:
            if jobname not in ["discord_mod", "fast_food_worker", "twitch_streamer", "youtuber", "pro_gamer", "teacher", "scientist", "doctor", "isobot_developer", "discord_employee"]: return "[1] That job name isn't valid!"
            userdat[str(id)]["job"] = jobname
            save()
        except KeyError: return "[!] That user might not be registered in the userdat repo yet! Try regestring the user first."
