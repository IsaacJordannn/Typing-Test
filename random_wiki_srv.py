import wikipedia
import time

def random_wiki_summary():
    # title of a random wiki page
    random = wikipedia.random(1)
    try:
        result = wikipedia.summary(random)
    except Exception as e:
        # try again if you get an error
        result = random_wiki_summary()
    return result

def communicate():
    result = random_wiki_summary()
    while len(result.split()) < 300:
        result = random_wiki_summary()

    while True:
        time.sleep(1.0)

        # open and read file
        f = open("random_wiki_service.txt", "r", encoding="utf-8", errors="ignore")
        line = f.readline()
        f.close()

        if line == "run":
            # erase file and write random wikipedia page summary
            f = open("random_wiki_service.txt", "w", encoding="utf-8")
            f.write(result)
            f.close()
            print("summary written to text file")
            communicate()


if __name__ == "__main__":
    communicate()