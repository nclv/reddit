# reddit

Save your reddit comments/posts informations in a JSON file.

# Setup

Create a `.env` file with the necessary credentials:
```bash
# .env
export CLIENT_ID=<your_client_id>
export CLIENT_SECRET=<your_client_secret>
export USER_AGENT="firefox:com.example.reddit-comments:v0.1.0 (by u/N0way00X2)"
export USERNAME=<your_username>
export PASSWORD=<your_password>
```

# Install
Install the requirements (`praw` and `python-dotenv`) and launch the script:
```bash
poetry install
poetry run python reddit_comments.py
```

Your saved comments and posts will be stored in `reddit-saved.json`:
```
[
	{
        "id": "t3_io2a16",
        "permalink": "/r/Unexpected/comments/io2a16/ah_yes_beer/",
        "title": "Ah yes beer",
        "content": "https://v.redd.it/gc9ur46b4ol51"
    },
    {
        "id": "t1_g4axe1b",
        "permalink": "/r/Jokes/comments/inzyna/an_alien_couple_land_their_saucer_in_a_farmers/g4axe1b/",
        "content": "Two aliens in space looking at Earth are talking to each other.\n\nThe first alien says, \"The dominant life forms>
    },
    {
        "id": "t3_inj3i6",
        "permalink": "/r/TwoSentenceHorror/comments/inj3i6/the_boy_asked_me_what_do_monsters_look_like/",
        "title": "The boy asked me, \"what do monsters look like?\"",
        "content": "The temptation to peel back his father's face and show him the truth was almost too much to bear."
    },
	...
]
```
