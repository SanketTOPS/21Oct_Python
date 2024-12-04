class master:
    def header(self,page):
        print(f"This is {page} page!")
    
class home(master):
    def header(self, page):
        return super().header(page)

class about(master):
    def header(self, page):
        return super().header(page)

class contact(master):
    def header(self, page):
        return super().header(page)
