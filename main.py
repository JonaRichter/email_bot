import smtplib, ssl
import csv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SENDER_EMAIL = "jonarichter@gmx.de"
SENDER_EMAIL_PASSWORD = "th278a31"
SENDER_NAME = "Kbrol"
SONG_TITLE = "Quiero Tequila"
SONG_LINK = "https://open.spotify.com/intl-de/track/1WwDJGrh7cBR5fohRUAut1?si=69ebd8715c8e4d3c"

with open("contacts_file.csv") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    for receiver_name, receiver_email, playlist_name in reader:
        # print(f"Sending email to {name}")
        
        # Send email here
        message = MIMEMultipart("alternative")
        message["Subject"] = f"Submission for Playlist Consideration: {SONG_TITLE} by {SENDER_NAME}"
        message["From"] = SENDER_EMAIL
        message["To"] = receiver_email
        
        # Create the plain-text and HTML version of your message
        text = f"""\
        Dear {receiver_name},

        I hope this message finds you well. My name is {SENDER_NAME}, and I am an emerging music producer striving to bring fresh and captivating sounds to audiences worldwide. I recently came across your curated playlist, {playlist_name}, on Spotify and was impressed by its eclectic selection and engagement with listeners.

        I wanted to take this opportunity to introduce you to my latest release, "{SONG_TITLE}" under the artist name {SENDER_NAME}. This track embodies [describe the essence or vibe of your song briefly, e.g., energetic beats, soulful melodies, etc.], and I believe it would resonate well with your playlist's audience.

        Here is the Spotify link to the song: {SONG_LINK}

        I would be honored if you could consider including "{SONG_TITLE}" in {playlist_name}. I am confident that it would complement the existing lineup and contribute positively to the listening experience for your subscribers.

        Thank you for your time and consideration. I look forward to any feedback you may have and the possibility of collaborating to bring great music to your audience.

        Warm regards,

        {SENDER_NAME}
        """
        html = f"""\
        <html>
        <body>
            <p>Dear {receiver_name},<br><br>
            I hope this message finds you well. My name is {SENDER_NAME}, and I am an emerging music producer striving to bring fresh and captivating sounds to audiences worldwide. I recently came across your curated playlist, {playlist_name}, on Spotify and was impressed by its eclectic selection and engagement with listeners.<br><br>
            I wanted to take this opportunity to introduce you to my latest release, "{SONG_TITLE}" under the artist name {SENDER_NAME}. This track embodies [describe the essence or vibe of your song briefly, e.g., energetic beats, soulful melodies, etc.], and I believe it would resonate well with your playlist's audience.<br><br>
            Here is the Spotify link to the song: <a href="{SONG_LINK}">{SONG_TITLE}</a><br><br>
            I would be honored if you could consider including "{SONG_TITLE}" in {playlist_name}. I am confident that it would complement the existing lineup and contribute positively to the listening experience for your subscribers.<br><br>
            Thank you for your time and consideration. I look forward to any feedback you may have and the possibility of collaborating to bring great music to your audience.<br><br>
            Warm regards,<br><br>
            {SENDER_NAME}
            </p>
        </body>
        </html>
        """

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        message.attach(part2)

        # Create a secure SSL context
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmx.net", 465, context=context) as server:
            server.login(SENDER_EMAIL, SENDER_EMAIL_PASSWORD)
            server.sendmail(
                SENDER_EMAIL, receiver_email, message.as_string()
            )
        print(f"Email sent to {receiver_name}")

