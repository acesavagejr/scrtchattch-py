import scratchattach as scratch3

session = scratch3.Session(".eJxVkM1ugzAQhN-Fc6HGP9jklhx6aKRWqdRDT8jAAg5gE-w0Uau-e9cSl1xnZr-d3d_k6mG1eoZkl2gPXn_rHs5r8pQEN4JFlUngRUc5kZryjta6UUI3NS-kJG0u6W46ntzlU6XBlukyqPr-Qg739P21PznETK43NjULkjCciSLLBcuoIOhV-hqGKjaoTIsBUQpGGWFotWdte1cFM8OPs7HdfobVNPr5DW7Vl1vHx_lB-yGuaHIFAkosBpKImrCuzHPOFGqyZEzygikieLwPfGicG02E3xAI7SMSL8UPxF5RAxtwezDOZpvhsw9Ypk08bOG_fxQba74:1r3TOq:5DN9OWxfGScCHao9XLBWo5vZ8iE", username="asesavagejr") 
conn = session.connect_cloud("925444079") 

client = scratch3.CloudRequests(conn)

@client.request
def online():
    print("online request recieved")
    return"yes"
@client.request
def foo(argument1):
    print(f"Data requested for user {argument1}")
    user = scratch3.get_user(argument1)
    stats = user.stats()
    return_data = []
    return_data.append(f"Total loves: {stats['loves']}")
    return_data.append(f"Total favorites: {stats['favorites']}")
    return_data.append(f"Total views: {stats['views']}")

    return return_data

@client.event
def on_ready():
    print("Request handler is running")

client.run() 