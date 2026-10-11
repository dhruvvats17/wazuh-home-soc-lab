# Editable architecture diagram source
# Run: python architecture/make_diagram.py
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
fig, ax = plt.subplots(figsize=(12, 7))
ax.set_xlim(0, 12); ax.set_ylim(0, 8); ax.axis("off")
def box(x,y,w,h,title,subtitle):
    p=FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.15,rounding_size=0.18",linewidth=1.6,edgecolor="black",facecolor="white")
    ax.add_patch(p)
    ax.text(x+w/2,y+h*0.65,title,ha="center",va="center",fontsize=12,fontweight="bold")
    ax.text(x+w/2,y+h*0.30,subtitle,ha="center",va="center",fontsize=9,wrap=True)
box(.6,5.2,4,1.45,"Windows 11 Endpoint","Wazuh Agent · Sysmon · Windows Event Logs")
box(7.4,5.2,4,1.45,"Ubuntu Server","Wazuh Manager · Indexer · Dashboard")
box(7.4,2.6,4,1.25,"SOC Analyst Workflow","Alert triage · Evidence review · Incident report")
box(.6,2.6,4,1.25,"Kali Linux Test Host","Authorized, controlled lab simulations")
ax.add_patch(FancyArrowPatch((4.7,5.92),(7.25,5.92),arrowstyle="-|>",mutation_scale=18,linewidth=1.6))
ax.text(5.98,6.25,"Configured telemetry",ha="center",fontsize=9)
ax.add_patch(FancyArrowPatch((9.4,5.05),(9.4,4.0),arrowstyle="-|>",mutation_scale=18,linewidth=1.6))
ax.text(9.65,4.55,"Alerts / events",ha="left",fontsize=9)
ax.add_patch(FancyArrowPatch((4.7,3.2),(7.25,3.2),arrowstyle="-|>",mutation_scale=18,linewidth=1.4,linestyle="dashed"))
ax.text(5.98,3.52,"Test traffic (not log ingestion)",ha="center",fontsize=8)
ax.text(6,7.35,"WAZUH HOME SOC LAB — ARCHITECTURE",ha="center",fontsize=16,fontweight="bold")
ax.text(6,.9,"Conceptual architecture. Confirm actual log sources, routing, and connectivity in the live lab.",ha="center",fontsize=9)
plt.tight_layout()
fig.savefig("architecture/lab-architecture.png",dpi=180,bbox_inches="tight")
