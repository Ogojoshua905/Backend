class FMM():
    FM = {}
    welcome = "Welcome! to Your Favourite Movie Manager" 
    def __init__(self, movie):
        self.movie = movie

    def add_movie(self, m_name, m_director, r_date):
        self.FM[m_name] = {
            "Director": m_director,
            "Release_Date": r_date
        }
    def remove_movie(self, m_name):
        if m_name in self.FM:
               del self.FM[m_name]
               print("Successful, Press Enter to continue....")
        else:
            print("Movie Not On Wishlist")

    def view_movie(self):
        if self.FM:
            for m_name, details in self.FM.items():
                print("=" * 8)
                print(f"Movie Name: {m_name}")
                print(f"Director: {details['Director']}")
                print(f"Release Date: {details['Release_Date']}")
                print("=" * 8)
        else:
            print("Movie Not In Database")
    def run_movie(self):
        print(self.welcome)
        while True:
            print("1. Add A Movie")
            print("2. Remove a Movie")
            print("3. View All Movies")
            print("4. Exit")
            FM = input("Choose From Option 1/2/3/4: ")
            if FM == "1":
                m_name = input("Enter Movie Name: ")
                m_director = input("The Movie was Directed By Whom: ")
                r_date = input("Year Of Released: ")
                self.add_movie(m_name, m_director, r_date)
                print("Movie Has Been Added to Watchlist Successful")
            elif FM == "2":
                m_name = input("Enter Movie Name: ")
                self.remove_movie(m_name)
            elif FM == "3":
                self.view_movie()
                input("Press Any Key to Continue")
            elif FM == "4":
                print("Exiting Programme")
                break
            else:
                print("Invalid Option. Please Use your Head......")
fmm = FMM("")
print(fmm.run_movie())