from pytube import YouTube
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def download(link):
    print("Title: ", link.title)
    print("Views: ", link.views)
    print("Length:", link.length, " seconds")

    video_format = link.streams.filter(progressive=True).get_highest_resolution()

    print("Downloading... ●ᴥ●")
    video_format.download()
    print("Your video has been downloaded")


if __name__ == '__main__':

    check = True

    while check:

        user_want = input("Would you like to download a video? (Yes / No)   ")

        if user_want == "Yes":
            url = input("Enter video URL here 〈(•ˇ‿ˇ•)-→")
            converted = YouTube(url)
            download(converted)
            break

        elif user_want == "No":
            print("The app will now close down.")
            check = False
            break

        # need to change the user input condition to stop it from satisfying the if statement and then rerun the loop
        elif user_want != "No" or user_want != "Yes":
            print("Only reply Yes or No")
            check = True
            continue

