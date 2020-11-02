import json
from bioblend import galaxy

# Load galaxy instance details
with open('galaxy-instance.json') as f:
    galaxy_instance_info = json.load(f)

# Connect with galaxy instance
galaxy_instance = galaxy.GalaxyInstance(url=galaxy_instance_info['galaxy_url'],
                                        key=galaxy_instance_info['user_api_key'])
# Get list of histories for the user
history_list = galaxy_instance.histories.get_histories()

# List of histories for the user
print(json.dumps(history_list, indent=4, sort_keys=True))

# Purge all the histories for the user
for history in history_list:
    history_id = history['id']
    galaxy_instance.histories.delete_history(history_id, purge=True)
    print('Purged history ' + history_id)
