# SystemDesign-Tail
Implementation of Tail -f for linux using WebSockets and Flask

Here server keeps a check on the file and keeps the track of changes.
The top 'N' lines from the end of the file are then send to the frontend using Sockets.

How to Run:
    pip install -r requirements.txt
    python server.py

Open index.html in a web browser.

