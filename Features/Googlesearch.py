from googlesearch import search

def google_search(Data):
    # get the search query from the user
    query = (Data)

    # perform the Google search
    for j in search(query, num_results=10):
        print(j)

# while True:
#     kk = input("Enter : ")
#     print(google_search(kk))