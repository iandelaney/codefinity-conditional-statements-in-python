bobs_age = 17
alices_age = 20
johns_age = 10
mikes_age = 18

# Checking if both Bob and John can enter the park
can_bob_and_john_enter = (bobs_age>=18) and (johns_age>=18)

# Checking if either Alice or Mike can enter the park
can_alice_or_mike_enter = (alices_age>=18) or (mikes_age>=18)

# Checking if Bob, Alice, and John can all enter the park together
can_bob_alice_john_enter = (alices_age>=18) or (bobs_age>=18) or (johns_age>=18)


# Testing
print("Can Bob and John enter the park together? ", can_bob_and_john_enter)
print("Can Alice or Mike enter the park? ", can_alice_or_mike_enter)
print("Can Bob, Alice and John all enter the park together? ", can_bob_alice_john_enter)