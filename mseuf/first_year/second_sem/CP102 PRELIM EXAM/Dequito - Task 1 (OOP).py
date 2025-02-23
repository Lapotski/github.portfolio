# -- CLASS TATTOO ARTIST --
class TattooArtist:
    def __init__(self, name: str, specialization: str, hourly_rate: float):
        self.__name = name
        self.__specialization = specialization
        self.__hourly_rate = hourly_rate
        
    # Getters
    @property
    def name(self):
        return self.__name
        
    @property
    def specialization(self):
        return self.__specialization
    
    @property
    def hourly_rate(self):
        return self.__hourly_rate
        
    # Setters
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and new_name.strip():
            self.__name = new_name
        else:
            raise ValueError("Invalid NAME!")
            
    @specialization.setter
    def specialization(self, new_specialization):
        if isinstance(new_specialization, str) and new_specialization.strip():
            self.__specialization = new_specialization
        else:
            raise ValueError("Invalid SPECIALIZATION!")
        
    @hourly_rate.setter
    def hourly_rate(self, new_rate):
        if isinstance(new_rate, (int, float)) and new_rate > 0:
            self.__hourly_rate = new_rate  
        else:
            raise ValueError("Invalid HOURLY RATE! Must be a positive number.")
            
    # Methods
    def display_artist_info(self):
        return (f'Tattoo Artist: {self.__name}\n'
                f'Artist Specialization: {self.__specialization}\n'
                f'Hourly Rate: ₱{self.__hourly_rate:.2f}')  


# -- CLASS TATTOO APPOINTMENT --
class TattooAppointment:
    def __init__(self, client_name: str, tat_design: str, duration: float, artist: TattooArtist):
        self.__client_name = client_name
        self.__tat_design = tat_design
        self.__duration = duration
        self.__artist = artist
        
    # Getters
    @property
    def client_name(self):
        return self.__client_name
    
    @property
    def tat_design(self):
        return self.__tat_design
    
    @property
    def duration(self):
        return self.__duration
    
    @property
    def artist(self):
        return self.__artist
    
    # Setters
    @client_name.setter
    def client_name(self, new_name):
        if isinstance(new_name, str) and new_name.strip():
            self.__client_name = new_name
        else:
            raise ValueError("Invalid CLIENT NAME!")
    
    @tat_design.setter
    def tat_design(self, new_design):
        if isinstance(new_design, str) and new_design.strip():
            self.__tat_design = new_design
        else:
            raise ValueError("Invalid TATTOO DESIGN!")
    
    @duration.setter
    def duration(self, new_duration):
        if isinstance(new_duration, (int, float)) and new_duration > 0:
            self.__duration = new_duration
        else:
            raise ValueError("Invalid DURATION! Must be a positive number.")
    
    @artist.setter
    def artist(self, new_artist: TattooArtist):
        if isinstance(new_artist, TattooArtist):
            self.__artist = new_artist
        else:
            raise ValueError("Invalid ARTIST!")

    # Methods
    def appointment_details(self):
        return (f'Appointment for {self.__client_name}\n'
                f'Tattoo Design: {self.__tat_design}\n'
                f'Duration: {self.__duration} hour(s)\n'
                f'Tattoo Artist: {self.__artist.name} ({self.__artist.specialization})')
        
    def calculate_cost(self):
        return self.__artist.hourly_rate * self.__duration


# -- MAIN PROGRAM --
artists = []
appointments = []

def main():
    while True:
        print("\nTattoo Studio Booking System")
        print("[1] Add Tattoo Artist")
        print("[2] View Tattoo Artists")
        print("[3] Book Tattoo Appointment")
        print("[4] View Appointments")
        print("[5] Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            add_tattoo_artist()
        elif choice == "2":
            display_artists()
        elif choice == "3":
            add_tattoo_appointment()
        elif choice == "4":
            display_appointments()
        elif choice == "5":
            print("\nExiting... Have a great day!")
            break
        else:
            print("Invalid choice. Please enter a number between 1-5.")


def add_tattoo_artist():
    print('\nAdd Tattoo Artist')
    name = input("Enter artist name: ").strip()
    specialization = input("Enter specialization: ").strip()
    
    while True:
        try:
            hourly_rate = float(input("Enter hourly rate (₱): "))
            if hourly_rate > 0:
                break
            else:
                print("Hourly rate must be a positive number.")
        except ValueError:
            print("Invalid input! Please enter a numeric value.")
    
    artist = TattooArtist(name, specialization, hourly_rate)
    artists.append(artist)
    print(f'Artist "{name}" has been added successfully!\n')


def add_tattoo_appointment():
    if not artists:
        print('\nNo tattoo artists available! Add an artist first.\n')
        return
    
    print('\nBook a Tattoo Appointment')
    client_name = input("Enter client name: ").strip()
    tat_design = input("Enter tattoo design: ").strip()
    
    while True:
        try:
            duration = float(input("Enter duration (in hours): "))
            if duration > 0:
                break
            else:
                print("Duration must be a positive number.")
        except ValueError:
            print("Invalid input! Please enter a numeric value.")
            
    print('\nAvailable Artists:')
    for i, artist in enumerate(artists, 1):
        print(f'{i}. {artist.name} - {artist.specialization} (₱{artist.hourly_rate}/hr)')
        
    while True:
        try:
            artist_choice = int(input("Select an artist by number: ")) - 1
            if 0 <= artist_choice < len(artists):
                break
            else:
                print("Invalid selection. Please enter a valid artist number.")
        except ValueError:
            print("Invalid input! Please enter a numeric value.")
    
    artist = artists[artist_choice]
    appointment = TattooAppointment(client_name, tat_design, duration, artist)
    appointments.append(appointment)
    
    print(f"\nAppointment for {client_name} booked with {artist.name}!\n")


def display_artists():
    if not artists:
        print("\nNo tattoo artists available.\n")
        return
    print("\nAvailable Tattoo Artists:")
    for i, artist in enumerate(artists, 1):
        print(f"{i}. {artist.display_artist_info()}\n")


def display_appointments():
    if not appointments:
        print("\nNo appointments scheduled.\n")
        return
    print("\nScheduled Appointments:")
    for i, appointment in enumerate(appointments, 1):
        print(f"{i}. {appointment.appointment_details()}")
        print(f"Total Cost: ₱{appointment.calculate_cost():.2f}\n")


# -- RUN PROGRAM --
if __name__ == "__main__":
    main()