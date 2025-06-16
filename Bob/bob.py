def response(hey_bob):
    hey_bob_refined=hey_bob.strip()
    if not hey_bob_refined:
         return "Fine. Be that way!"
    elif hey_bob_refined.isupper()and hey_bob_refined.endswith('?'):
         return "Calm down, I know what I'm doing!"
    elif hey_bob_refined.isupper():
         return "Whoa, chill out!"
    elif hey_bob_refined.endswith('?'):
         return  "Sure."
    else:
         return "Whatever."