import scratchattach as scratch3

session = scratch3.Session(".eJxVkM1ugzAQhN-Fc6HGP9jklhx6aKRWqdRDT8jAAg5gE-w0Uau-e9cSl1xnZr-d3d_k6mG1eoZkl2gPXn_rHs5r8pQEN4JFlUngRUc5kZryjta6UUI3NS-kJG0u6W46ntzlU6XBlukyqPr-Qg739P21PznETK43NjULkjCciSLLBcuoIOhV-hqGKjaoTIsBUQpGGWFotWdte1cFM8OPs7HdfobVNPr5DW7Vl1vHx_lB-yGuaHIFAkosBpKImrCuzHPOFGqyZEzygikieLwPfGicG02E3xAI7SMSL8UPxF5RAxtwezDOZpvhsw9Ypk08bOG_fxQba74:1r3TOq:5DN9OWxfGScCHao9XLBWo5vZ8iE", username="asesavagejr") 
conn = session.connect_cloud("925395054") 

client = scratch3.CloudRequests(conn)

@client.request
def online(): #called when client receives request
    print("online request received")
    return "yes"

@client.request
def message_count(argument1):
    print(f"Message count requested for user {argument1}")
    user = scratch3.get_user(argument1)
    return user.message_count()

@client.event
def on_ready():
    print("Request handler is running")

client.run() 