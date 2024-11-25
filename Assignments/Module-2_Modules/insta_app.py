import instaloader

instaID=input("Enter an instagram ID:")

insta=instaloader.Instaloader()
insta.download_profile(instaID)
print("Download successfully!")