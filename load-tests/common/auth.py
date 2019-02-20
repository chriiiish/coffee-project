def login(self):
  print("Logging in")
  self.client.post("/login", {"Username": "uname", "Password": "pwd"})

def logout(self):
  print("Logging out")
  self.client.get("/logout")