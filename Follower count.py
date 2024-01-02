import scratchattach as scratch3
import time

session = scratch3.login("asesavagejr", "aidenaiden8")
user = session.get_linked_user()

while True:
    follower_count = user.follower_count()
    user.set_bio(f"꒦︶꒷꒦꒷︶︶꒷꒦꒷︶꒦꒷︶︶꒷꒦꒷꒦꒦︶꒷꒦꒷︶︶꒷꒦︶I make games and animations.I use gandi ide to code on scratchF4F❌My follower count: {follower_count}")
    time.sleep(20) # The follower count is updated every 60 seconds