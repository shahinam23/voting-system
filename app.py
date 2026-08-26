import streamlit as st


# ============================================
# ORGANIZATION / SCHOOL VOTING SYSTEM
# ============================================

# Shared application data
@st.cache_resource
def get_data():
    return {
        "admin": {
            "username": "admin",
            "password": "admin123"
        },

        "voters": {
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
        },

        "candidates": {
            "President": [
                "candidate.1",
                "candidate.2"
            ],
            "Secretary": [
                "candidate.3",
                "candidate.4"
            ]
        },

        "candidate_details": {
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
        },

        "votes": {
            "President": {
                "candidate.1": 0,
                "candidate.2": 0
            },
            "Secretary": {
                "candidate.3": 0,
                "candidate.4": 0
            }
        },

        "election": {
            "name": "School Club Elections",
            "active": False
        }
    }


data = get_data()


# ============================================
# PAGE SETTINGS
# ============================================

st.set_page_config(
    page_title="Voting System",
    page_icon="🗳️",
    layout="centered"
)


# ============================================
# TITLE
# ============================================

st.title("🗳️ School / Organization Voting System")
st.write("A simple electronic voting system.")


# ============================================
# SESSION STATE
# ============================================

if "page" not in st.session_state:
    st.session_state.page = "home"

if "logged_in_voter" not in st.session_state:
    st.session_state.logged_in_voter = None

if "admin_logged_in" not in st.session_state:
    st.session_state.admin_logged_in = False


# ============================================
# HOME PAGE
# ============================================

def home_page():

    st.subheader("Welcome!")

    st.write("Please choose how you want to enter the system.")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("👨‍💼 Administrator", use_container_width=True):
            st.session_state.page = "admin_login"
            st.rerun()

    with col2:
        if st.button("🗳️ Voter", use_container_width=True):
            st.session_state.page = "voter_login"
            st.rerun()


# ============================================
# ADMIN LOGIN
# ============================================

def admin_login():

    st.header("👨‍💼 Administrator Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login", use_container_width=True):

        if (
            username == data["admin"]["username"]
            and password == data["admin"]["password"]
        ):
            st.session_state.admin_logged_in = True
            st.session_state.page = "admin_dashboard"
            st.rerun()

        else:
            st.error("Incorrect username or password.")

    if st.button("⬅️ Back"):
        st.session_state.page = "home"
        st.rerun()


# ============================================
# ADMIN DASHBOARD
# ============================================

def admin_dashboard():

    st.header("👨‍💼 Admin Dashboard")

    st.success("Administrator logged in.")

    st.subheader("Election")

    st.write("Current election:", data["election"]["name"])

    if data["election"]["active"]:
        st.success("🟢 Election is ACTIVE")
    else:
        st.warning("🔴 Election is CLOSED")

    # ----------------------------------------
    # Create election
    # ----------------------------------------

    with st.expander("Create / Rename Election"):

        election_name = st.text_input(
            "Election name",
            value=data["election"]["name"]
        )

        if st.button("Save Election Name"):

            if election_name.strip():
                data["election"]["name"] = election_name.strip()
                st.success("Election name updated.")
                st.rerun()

    # ----------------------------------------
    # Start / End election
    # ----------------------------------------

    col1, col2 = st.columns(2)

    with col1:

        if st.button("▶️ Start Election", use_container_width=True):

            if data["election"]["active"]:
                st.warning("Election is already active.")
            else:
                data["election"]["active"] = True
                st.success("Election has started.")
                st.rerun()

    with col2:

        if st.button("⏹️ End Election", use_container_width=True):

            if not data["election"]["active"]:
                st.warning("Election is already closed.")
            else:
                data["election"]["active"] = False
                st.success("Election has ended.")
                st.rerun()

    # ----------------------------------------
    # Register voter
    # ----------------------------------------

    with st.expander("➕ Register Voter"):

        voter_id = st.text_input("Voter ID")
        voter_name = st.text_input("Voter Name")
        voter_password = st.text_input(
            "Voter Password",
            type="password"
        )

        if st.button("Register Voter"):

            if not voter_id or not voter_name or not voter_password:
                st.error("Please fill in all fields.")

            elif voter_id in data["voters"]:
                st.error("This voter already exists.")

            else:

                data["voters"][voter_id] = {
                    "name": voter_name,
                    "password": voter_password,
                    "eligible": True,
                    "voted": False
                }

                st.success("Voter registered successfully.")
                st.rerun()

    # ----------------------------------------
    # Register candidate
    # ----------------------------------------

    with st.expander("➕ Register Candidate"):

        candidate_id = st.text_input("Candidate ID")
        candidate_name = st.text_input("Candidate Name")
        position = st.text_input("Position")

        if st.button("Register Candidate"):

            if not candidate_id or not candidate_name or not position:
                st.error("Please fill in all fields.")

            elif candidate_id in data["candidate_details"]:
                st.error("This candidate already exists.")

            else:

                data["candidate_details"][candidate_id] = {
                    "name": candidate_name,
                    "position": position
                }

                if position not in data["candidates"]:
                    data["candidates"][position] = []

                data["candidates"][position].append(candidate_id)

                if position not in data["votes"]:
                    data["votes"][position] = {}

                data["votes"][position][candidate_id] = 0

                st.success("Candidate registered successfully.")
                st.rerun()

    # ----------------------------------------
    # View candidates
    # ----------------------------------------

    st.subheader("👥 Candidates")

    for position in data["candidates"]:

        st.write(f"### {position}")

        for candidate_id in data["candidates"][position]:

            candidate_name = data["candidate_details"][candidate_id]["name"]

            st.write(
                f"• {candidate_name} ({candidate_id})"
            )

    # ----------------------------------------
    # View voters
    # ----------------------------------------

    st.subheader("👤 Registered Voters")

    for voter_id, voter in data["voters"].items():

        if voter["voted"]:
            status = "✅ Already Voted"
        else:
            status = "⏳ Not Voted"

        st.write(
            f"**{voter['name']}** — `{voter_id}` — {status}"
        )

    # ----------------------------------------
    # Results
    # ----------------------------------------

    st.subheader("📊 Election Results")

    if data["election"]["active"]:

        st.info("Results cannot be displayed while the election is active.")

    else:

        for position in data["votes"]:

            st.write(f"### {position}")

            highest_votes = -1
            winners = []

            for candidate_id, vote_count in data["votes"][position].items():

                candidate_name = data["candidate_details"][candidate_id]["name"]

                st.write(
                    f"**{candidate_name}:** {vote_count} vote(s)"
                )

                if vote_count > highest_votes:

                    highest_votes = vote_count
                    winners = [candidate_id]

                elif vote_count == highest_votes:

                    winners.append(candidate_id)

            if len(winners) == 1:

                winner_name = data["candidate_details"][winners[0]]["name"]

                st.success(
                    f"🏆 Winner: {winner_name}"
                )

            else:

                st.warning("Result: TIE")

                for winner_id in winners:

                    winner_name = data["candidate_details"][winner_id]["name"]

                    st.write(f"• {winner_name}")

    # ----------------------------------------
    # Logout
    # ----------------------------------------

    st.divider()

    if st.button("Logout"):

        st.session_state.admin_logged_in = False
        st.session_state.page = "home"
        st.rerun()


# ============================================
# VOTER LOGIN
# ============================================

def voter_login():

    st.header("🗳️ Voter Login")

    if not data["election"]["active"]:

        st.warning("Voting is currently closed.")

        if st.button("⬅️ Back"):
            st.session_state.page = "home"
            st.rerun()

        return

    voter_id = st.text_input("Voter ID")
    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login", use_container_width=True):

        if voter_id not in data["voters"]:

            st.error("Voter does not exist.")

        else:

            voter = data["voters"][voter_id]

            if voter["password"] != password:

                st.error("Incorrect password.")

            elif not voter["eligible"]:

                st.error("You are not eligible to vote.")

            elif voter["voted"]:

                st.error("You have already voted.")

            else:

                st.session_state.logged_in_voter = voter_id
                st.session_state.page = "vote"
                st.rerun()

    if st.button("⬅️ Back"):

        st.session_state.page = "home"
        st.rerun()


# ============================================
# VOTING PAGE
# ============================================

def voting_page():

    voter_id = st.session_state.logged_in_voter

    if voter_id is None:
        st.session_state.page = "home"
        st.rerun()

    voter = data["voters"][voter_id]

    st.header("🗳️ Cast Your Vote")

    st.success(f"Welcome, {voter['name']}!")

    if not data["election"]["active"]:

        st.error("The election has ended.")
        return

    selected_votes = {}

    for position in data["candidates"]:

        st.subheader(position)

        candidate_ids = data["candidates"][position]

        candidate_names = [
            data["candidate_details"][candidate_id]["name"]
            for candidate_id in candidate_ids
        ]

        selected_name = st.radio(
            f"Choose your {position} candidate:",
            candidate_names,
            key=f"vote_{position}"
        )

        for candidate_id in candidate_ids:

            if data["candidate_details"][candidate_id]["name"] == selected_name:

                selected_votes[position] = candidate_id

    st.divider()

    st.subheader("Review Your Vote")

    for position, candidate_id in selected_votes.items():

        candidate_name = data["candidate_details"][candidate_id]["name"]

        st.write(
            f"**{position}:** {candidate_name}"
        )

    if st.button(
        "✅ Submit Vote",
        use_container_width=True
    ):

        for position, candidate_id in selected_votes.items():

            data["votes"][position][candidate_id] += 1

        data["voters"][voter_id]["voted"] = True

        st.session_state.logged_in_voter = None
        st.session_state.page = "vote_success"

        st.rerun()


# ============================================
# VOTE SUCCESS
# ============================================

def vote_success():

    st.header("✅ Vote Submitted")

    st.success(
        "Your vote has been recorded successfully!"
    )

    st.write(
        "You cannot vote again with this voter account."
    )

    if st.button("Return to Home"):

        st.session_state.page = "home"
        st.rerun()


# ============================================
# PAGE ROUTING
# ============================================

if st.session_state.page == "home":

    home_page()

elif st.session_state.page == "admin_login":

    admin_login()

elif st.session_state.page == "admin_dashboard":

    if st.session_state.admin_logged_in:

        admin_dashboard()

    else:

        st.session_state.page = "admin_login"
        st.rerun()

elif st.session_state.page == "voter_login":

    voter_login()

elif st.session_state.page == "vote":

    voting_page()

elif st.session_state.page == "vote_success":

    vote_success()