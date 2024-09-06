""" Main entry point for the Lightning AI Orchestrator """

from lightning_sdk import Studio, Teamspace, User, Organization
from dotenv import load_dotenv
import os

load_dotenv()

LIGHTNING_API_KEY = os.getenv("LIGHTNING_API_KEY")
# LIGHTNING_USER_ID = "entangleit"
LIGHTNING_ORG_ID = os.getenv("LIGHTNING_ORG_ID")
LIGHTNING_TEAMSPACE_ID = os.getenv("LIGHTNING_TEAMSPACE_ID")
LIGHTNING_STUDIO_ID = os.getenv("LIGHTNING_STUDIO_ID")
print(LIGHTNING_STUDIO_ID)
print(LIGHTNING_TEAMSPACE_ID)
# print(LIGHTNING_USER_ID)
print(LIGHTNING_ORG_ID)

# allows interaction with the Studio in the Teamspace of org
s = Studio(LIGHTNING_STUDIO_ID, teamspace=LIGHTNING_TEAMSPACE_ID, org=LIGHTNING_ORG_ID)

# allows interaction with Teamspace of organization
t = Teamspace(LIGHTNING_TEAMSPACE_ID, org=LIGHTNING_ORG_ID)

# allows interaction with user
# u = User("entangleit")
# print(u.teamspaces)
# allows interaction with organization
o = Organization(LIGHTNING_ORG_ID)

print("Organization Teamspaces:\n")
print(o.teamspaces)

print("Studio name: " + s.name)
