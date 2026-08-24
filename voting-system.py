# ============================================
# ORGANIZATION / SCHOOL VOTING SYSTEM
# ============================================

admin = {
    "username": "admin",    #admin is the dictionary used in python:it takes key-value pairs
    "password": "admin123"
    }

# Voter information
voters = {      # python uses nested dictionary in this step: dictionaries inside dictionary
    "voter.1": {
        "name": "Rehmat",
        "password": "1234",
        "eligible": True,
        "voted": False
    },
    "voter.2": {
        "name": "Aliyan",
        "password": "1234",
        "eligible": True,
        "voted": False
    },
    "voter.3": {
        "name": "Zuhaib",
        "password": "1234",
        "eligible": True,
        "voted": False
    },
    "voter.4": {
        "name": "Ryhaan",
        "password": "1234",
        "eligible": True,
        "voted": False
    },
    "voter.5": {
        "name": "Azhar",
        "password": "1234",
        "eligible": True,
        "voted": False
    }
}

# Candidate information
candidates = {
    "President": [
        "candidate.1",
        "candidate.2"
    ],
    "Secretary": [
        "candidate.3",
        "candidate.4"
    ]
}

# Candidate details
candidate_details = {
    "candidate.1": {
        "name": "Inam",
        "position": "President"
    },
    "candidate.2": {
        "name": "Fayzan",
        "position": "President"
    },
    "candidate.3": {
        "name": "Zara",
        "position": "Secretary"
    },
    "candidate.4": {
        "name": "Sara",
        "position": "Secretary"
    }
}

# Vote count
votes = {
    "President": {
        "candidate.1": 0,
        "candidate.2": 0
    },
    "Secretary": {
        "candidate.3": 0,
        "candidate.4": 0
    }
}

# Election information
election = {
    "name": "School Club Elections",
    "active": False
}

# Admin login
def admin_login():
    print("\n========== ADMIN LOGIN ==========")
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == admin["username"] and password == admin["password"]:
        print("\nAdmin login successful!")
        return True
    else:
        print("\nIncorrect username or password.")
        return False

# Create election
def create_election():
    print("\n========== CREATE ELECTION ==========")
    election_name = input("Enter election name: ")
    election["name"] = election_name
    print("\nElection created successfully!")
    print("Election:", election["name"])

# Register voter
def register_voter():
    print("\n========== REGISTER VOTER ==========")
    voter_id = input("Enter voter ID: ")

    if voter_id in voters:
        print("\nThis voter already exists.")
        return

    name = input("Enter voter name: ")
    password = input("Create password: ")

    voters[voter_id] = {
        "name": name,
        "password": password,
        "eligible": True,
        "voted": False
    }

    print("\nVoter registered successfully!")

# Register candidate
def register_candidate():
    print("\n========== REGISTER CANDIDATE ==========")
    candidate_id = input("Enter candidate ID: ")

    if candidate_id in candidate_details:
        print("\nThis candidate already exists.")
        return

    name = input("Enter candidate name: ")
    position = input("Enter position: ")

    candidate_details[candidate_id] = {
        "name": name,
        "position": position
    }

    if position not in candidates:
        candidates[position] = []

    candidates[position].append(candidate_id)

    if position not in votes:
        votes[position] = {}

    votes[position][candidate_id] = 0

    print("\nCandidate registered successfully!")

# View candidates
def view_candidates():
    print("\n========== CANDIDATES ==========")

    for position in candidates:
        print("\nPosition:", position)

        for candidate_id in candidates[position]:
            candidate_name = candidate_details[candidate_id]["name"]
            print(candidate_id, "-", candidate_name)

# View voters
def view_voters():
    print("\n========== REGISTERED VOTERS ==========")

    for voter_id in voters:
        voter_name = voters[voter_id]["name"]

        if voters[voter_id]["voted"]:
            status = "Already Voted"
        else:
            status = "Not Voted"

        print(voter_id, "-", voter_name, "-", status)

# Start election
def start_election():
    print("\n========== START ELECTION ==========")

    if election["active"]:
        print("\nElection is already active.")
        return

    election["active"] = True
    print("\nElection has started!")
    print("Election:", election["name"])

# End election
def end_election():
    print("\n========== END ELECTION ==========")

    if not election["active"]:
        print("\nElection is not currently active.")
        return

    election["active"] = False
    print("\nElection has ended!")

# Voter login
def voter_login():
    print("\n========== VOTER LOGIN ==========")
    voter_id = input("Enter voter ID: ")
    password = input("Enter password: ")

    if voter_id not in voters:
        print("\nVoter does not exist.")
        return None

    voter = voters[voter_id]

    if voter["password"] != password:
        print("\nIncorrect password.")
        return None

    if voter["eligible"] == False:
        print("\nYou are not eligible to vote.")
        return None

    if voter["voted"] == True:
        print("\nYou have already voted.")
        return None

    print("\nWelcome,", voter["name"])
    return voter_id

# Cast vote
def cast_vote(voter_id):
    print("\n========== CAST YOUR VOTE ==========")
    selected_votes = {}

    for position in candidates:
        print("\nPosition:", position)

        for candidate_id in candidates[position]:
            candidate_name = candidate_details[candidate_id]["name"]
            print(candidate_id, "-", candidate_name)

        while True:
            choice = input("Enter candidate ID: ")

            if choice in candidates[position]:
                selected_votes[position] = choice
                break
            else:
                print("Invalid candidate ID. Please try again.")

    # Review vote
    print("\n========== REVIEW YOUR VOTE ==========")

    for position in selected_votes:
        candidate_id = selected_votes[position]
        candidate_name = candidate_details[candidate_id]["name"]
        print(position, "->", candidate_name)

    # Confirm vote
    confirmation = input("\nAre you sure you want to submit? (yes/no): ")

    if confirmation.lower() != "yes":
        print("\nVote cancelled.")
        return

    # Save vote
    for position in selected_votes:
        candidate_id = selected_votes[position]
        votes[position][candidate_id] += 1

    voters[voter_id]["voted"] = True

    print("\nYour vote has been recorded!")
    print("You cannot vote again.")

# Show results
def show_results():
    print("\n========================================")
    print("           ELECTION RESULTS")
    print("========================================")

    if election["active"]:
        print("\nElection is still active.")
        print("Results cannot be displayed yet.")
        return

    for position in votes:
        print("\nPosition:", position)
        print("--------------------------------")

        highest_votes = -1
        winners = []

        for candidate_id in votes[position]:
            vote_count = votes[position][candidate_id]
            candidate_name = candidate_details[candidate_id]["name"]

            print(candidate_name, ":", vote_count, "vote(s)")

            if vote_count > highest_votes:
                highest_votes = vote_count
                winners = [candidate_id]
            elif vote_count == highest_votes:
                winners.append(candidate_id)

        if len(winners) == 1:
            winner_id = winners[0]
            winner_name = candidate_details[winner_id]["name"]
            print("\nWinner:", winner_name)
        else:
            print("\nResult: TIE")
            print("Candidates tied:")

            for winner_id in winners:
                print("-", candidate_details[winner_id]["name"])

# Admin dashboard
def admin_dashboard():
    while True:
        print("\n========================================")
        print("            ADMIN DASHBOARD")
        print("========================================")
        print("1. Create Election")
        print("2. Register Voter")
        print("3. Register Candidate")
        print("4. View Candidates")
        print("5. View Voters")
        print("6. Start Election")
        print("7. End Election")
        print("8. View Results")
        print("9. Logout")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            create_election()
        elif choice == "2":
            register_voter()
        elif choice == "3":
            register_candidate()
        elif choice == "4":
            view_candidates()
        elif choice == "5":
            view_voters()
        elif choice == "6":
            start_election()
        elif choice == "7":
            end_election()
        elif choice == "8":
            show_results()
        elif choice == "9":
            print("\nLogging out...")
            break
        else:
            print("\nInvalid choice.")

# Voter dashboard
def voter_dashboard():
    if not election["active"]:
        print("\nVoting is currently closed.")
        return

    voter_id = voter_login()

    if voter_id is None:
        return

    cast_vote(voter_id)

# Main program
def main():
    while True:
        print("\n========================================")
        print("       SCHOOL / ORGANIZATION")
        print("            VOTING SYSTEM")
        print("========================================")
        print("1. Administrator")
        print("2. Voter")
        print("3. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            if admin_login():
                admin_dashboard()
        elif choice == "2":
            voter_dashboard()
        elif choice == "3":
            print("\nThank you for using the Voting System!")
            break
        else:
            print("\nInvalid choice. Please try again.")

# Start program
if __name__ == "__main__":
    main()
