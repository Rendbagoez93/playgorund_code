# Step 1: Define user profiles with video game characters
users = [
    {"name": "Link", "location": ("Hyrule", "Fantasy Realm"), "interests": {"sword fighting", "puzzles", "exploration"}},
    {"name": "Mario", "location": ("Mushroom Kingdom", "Fantasy Realm"), "interests": {"jumping", "racing", "exploration"}},
    {"name": "Lara Croft", "location": ("London", "Earth"), "interests": {"exploration", "puzzles", "archaeology"}},
    {"name": "Master Chief", "location": ("Reach", "Outer Space"), "interests": {"combat", "strategy", "exploration"}}
]

# Add new user function
def add_new_user():
    name = input("Enter character name: ")
    city = input("Enter character location (City): ")
    realm = input("Enter character location (Realm): ")
    interests_input = input("Enter interests (comma-separated): ")

    interests = set(interests_input.strip().split(","))
    new_user = {"name": name, "location": (city, realm), "interests": {i.strip() for i in interests}}

    users.append(new_user)
    print(f"\n✅ Added {name} to the roster!\n")

# Compare all users
def compare_all_users(user_list):
    for i in range(len(user_list)):
        for j in range(i + 1, len(user_list)):
            user1 = user_list[i]
            user2 = user_list[j]
            shared = user1["interests"] & user2["interests"]
            if shared:
                print(f"{user1['name']} & {user2['name']} share: {', '.join(shared)}")

# Add and compare loop
while True:
    add_new_user()
    print("\n🔍 Updated Shared Interests:\n")
    compare_all_users(users)
    more = input("\nAdd another character? (yes/no): ")
    if more.lower() != "yes":
        break
print("\nThank you for using the character interest comparison tool!")
# End of Main4.py
# This script allows users to add new video game characters and compare their interests.