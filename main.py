""" Main entry point for the Lightning AI Orchestrator """

from lightning_sdk import Studio, Teamspace, User, Organization
from dotenv import load_dotenv
import os

load_dotenv()

LIGHTNING_API_KEY = os.getenv("LIGHTNING_API_KEY")
LIGHTNING_USER_ID = os.getenv("LIGHTNING_USER_ID")
LIGHTNING_ORG_ID = os.getenv("LIGHTNING_ORG_ID")
LIGHTNING_TEAMSPACE_ID = os.getenv("LIGHTNING_TEAMSPACE_ID")
LIGHTNING_STUDIO_ID = os.getenv("LIGHTNING_STUDIO_ID")
print(LIGHTNING_STUDIO_ID)
print(LIGHTNING_TEAMSPACE_ID)
print(LIGHTNING_USER_ID)
print(LIGHTNING_ORG_ID)

# allows interaction with the Studio named "my-studio" in the Teamspace "train-model" of user "zeus"
s = Studio(LIGHTNING_STUDIO_ID, teamspace=LIGHTNING_TEAMSPACE_ID, user=LIGHTNING_USER_ID)

# allows interaction with Teamspace "train-model" of organization "olymp"
t = Teamspace(LIGHTNING_TEAMSPACE_ID, user=LIGHTNING_USER_ID)

# allows interaction with user "zeus"
u = User(LIGHTNING_USER_ID)
print(u.teamspaces)
# allows interaction with organization "olymp"
o = Organization(LIGHTNING_ORG_ID)

print(s.name)
