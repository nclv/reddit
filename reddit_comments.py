import os

from dotenv import load_dotenv
import praw
import json

load_dotenv(verbose=True)

CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
USER_AGENT = os.environ.get("USER_AGENT")
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")


def get_json():
    """Load JSON file content if the file exist. Else it returns an empty list.

    Returns:    
        json_content (list): Content of JSON file or [],
    """

    try:
        with open("reddit-saved.json", "r", encoding='utf-8') as file:
            json_content = json.load(file)
        print(f"Chargement du fichier JSON.")
    except FileNotFoundError:
        print("Création du fichier JSON.")
        json_content = []

    return json_content


def get_entries(reddit, last_id):
    """Return a list of choosen attributes from saved comments/posts.

    Args:
        reddit (praw.Reddit): PRAW reddit instance,
        last_id (str): ID of the last comment/post already in the JSON file,

    Returns:
        new_data (list[dict]): Comments and posts useful attributes,       
    """

    new_entry_count = 0
    new_data = []
    for item in reddit.user.me().saved(limit=None, params={"after": last_id}):
        data = {}
        # pprint(vars(item))
        data["id"] = item.name
        if isinstance(item, praw.models.Submission):
            # Posts item.name is t3_<id>
            data["permalink"] = item.permalink
            data["title"] = item.title
            if item.is_self:
                data["content"] = item.selftext
            else:
                data["content"] = item.url
        else:
            # Comments item.name is t1_<id>
            # print("post_author :", item.author)
            # item.id and comment's author is in the permalink
            data["permalink"] = item.permalink  # https://www.reddit.com<permalink>
            data["content"] = item.body
        new_data.append(data)
        new_entry_count += 1
    print(f"Nombre d'entrées ajoutées: {new_entry_count}")

    return new_data


def save_json(all_data):
    """Overwrite the JSON file.

    Args:
        all_data (list[dict]): Content to write,
    """

    with open("reddit-saved.json", "w", encoding='utf-8') as file:
        json.dump(all_data, file, ensure_ascii=False, indent=4)

def main():
    """ main function """

    reddit = praw.Reddit(client_id=CLIENT_ID,
                         client_secret=CLIENT_SECRET,
                         user_agent=USER_AGENT,
                         username=USERNAME,
                         password=PASSWORD)
    
    print(f"Utilisateur: {reddit.user.me()}")
    print(f"Read-only: {reddit.read_only}")
    
    json_content = get_json()
    last_id = json_content[-1]["id"] if json_content else None
    entries_count = len(json_content) if json_content else 0

    print(f"Nombre d'entrées: {entries_count}")

    new_data = get_entries(reddit, last_id)
    if new_data: save_json(json_content + new_data)

if __name__ == "__main__":
    main()
