

class RefChangeRequest:
    def __init__(self, repo_name: str, repo_link: str, update_type: str, to_hash: str, from_hash: str, ref_id: str):
        self.repo_name = repo_name
        self.repo_link = repo_link
        self.update_type = update_type
        self.to_hash = to_hash
        self.from_hash = from_hash
        self.ref_id = ref_id
