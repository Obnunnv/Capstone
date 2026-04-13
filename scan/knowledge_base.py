SERVICE_INFO = {
    "ssh": {
        "risk": "MEDIUM",
        "description": "SSH allows secure remote login into the system.",
        "danger": "If exposed, attackers can attempt brute-force login attacks.",
        "fix": "Disable if unused, or restrict access and use key-based authentication instead of passwords."
    },

    "http": {
        "risk": "LOW",
        "description": "HTTP is a web server protocol used to serve websites.",
        "danger": "Unencrypted traffic can be intercepted or modified.",
        "fix": "Use HTTPS instead or restrict exposure to trusted networks."
    },

    "ipp": {
        "risk": "LOW",
        "description": "IPP is used for network printing services.",
        "danger": "Usually low risk, but unnecessary exposure can reveal network services.",
        "fix": "Disable if printing is not needed or restrict to local network."
    }
}
