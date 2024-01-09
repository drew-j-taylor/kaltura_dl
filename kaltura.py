import requests

PID = 1832361
BASE_URL = f"https://cfvod.kaltura.com/pd/p/{PID}/sp/{PID}00/serveFlavor/entryId/"

def construct_url(entry_id, flavor_id, date, clas, suffix):
    return f"{BASE_URL}{entry_id}/v/1/ev/3/flavorId/{flavor_id}/name/{date}_{clas}_{suffix}.mp4"

def download_video(url):
    """
    Downloads a video from the given URL and saves it locally.
    """
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        filename = url.split('/')[-1]
        with open(filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192): 
                file.write(chunk)

        return f"Video downloaded successfully as {filename}"
    except requests.RequestException as e:
        return f"An error occurred: {e}"

def main():
    date = input("Enter date: ")
    clas = input("Enter class code: ")
    parent = input("Enter recording entry: ")
    extract1 = input("Enter first extracted url: ")
    extract2 = input("Enter second extracted url: ")

    entry_id1, flavor_id1 = extract1[73:83], extract1[102:112]
    entry_id2, flavor_id2 = extract2[73:83], extract2[102:112]

    suffix1, suffix2 = ("x", "y") if parent not in (entry_id1, entry_id2) else ("projector", "classroom")
    
    url1 = construct_url(entry_id1, flavor_id1, date, clas, suffix1)
    url2 = construct_url(entry_id2, flavor_id2, date, clas, suffix2)

    print(download_video(url1))
    print(download_video(url2))

if __name__ == "__main__":
    main()
