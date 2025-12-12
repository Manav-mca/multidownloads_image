import multiprocessing
import requests
# import concurrent.futures
def donwloadFile(url, name):
    print(f"started Donwloading {name} ")
    
    response = requests.get(url)
    open(f"files/file{name}.jpg", "wb").write(response.content)
    print(f"finished Downloading{name}")


if __name__ == "__main__":

    url = "https://picsum.photos/2000/3000"
    pros = []
    for i in range(5):
        donwloadFile(url, i)

    #     p = multiprocessing.Process(target=donwloadFile, args=[url, i])
    #     p.start()
    #     pros.append(p)

    # for p in pros:
    #     p.join()


# # import multiprocessing
# import requests
# import concurrent.futures


# def downloadFile(url, name):
#     print(f"started Downloading {name}")
#     response = requests.get(url)
#     open(f"files/file{name}.jpg", "wb").write(response.content)
#     print(f"finished Downloading {name}")

# if __name__ == "__main__":
#     url = "https://picsum.photos/2000/3000"
#     # pros = []
#     # for i in range(10):
#     #     p = multiprocessing.Process(target=downloadFile, args=[url, i])
#     #     p.start()
#     #     pros.append(p)

#     # for p in pros:
#     #     p.join()

#     with concurrent.futures.ProcessPoolExecutor() as executor:
#         l1 = [i for i in range(30)]
#         l2 = [url for i in range (30)]
#         results = executor.map(downloadFile, url, l1, l2)
#         for r in results:
#             print(r)
    
