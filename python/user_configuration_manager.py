def add_setting(settings:dict, new_setting:tuple):
    new_key, new_value = new_setting
    
    key, value = new_key.lower(), new_value.lower()

    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        settings[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(settings: dict, new_setting: tuple):
    new_key, new_value = new_setting
    key, value = new_key.lower(), new_value.lower()

    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else: 
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."


def delete_setting(settings:dict, key_to_delete):
    key_to_delete = key_to_delete.lower()

    if key_to_delete in settings: 
        del settings[key_to_delete]
        return f"Setting '{key_to_delete}' deleted successfully!"
    else:
        return "Setting not found!"


def view_settings(settings:dict):
    if not settings:
        return "No settings available."
    else:
        output = "Current User Settings:\n"
        for key, value in settings.items():
            output += f"{key.capitalize()}: {value}\n"
        return output



if __name__ == "__main__":
    test_settings = {'size': '200'}
    print(add_setting({'theme': 'light'}, ('THEME', 'dark')))
    print(add_setting({'theme': 'light'}, ('volume', 'high')))
    print(update_setting({'theme': 'light'}, ('theme', 'dark'))) 
    print(delete_setting({'theme': 'light'}, 'theme'))
    print(view_settings(""))