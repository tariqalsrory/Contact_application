
## ------------------------------------ ##
# -- this is programe for contact application -- #
# -------------------------------------- ##

import json
## -- class for contact 

class Contact:
    
    def __init__(self ,id ,name ,mobile ,emial):
        self.id = id
        self.name = name
        self.mobile = mobile
        self.emial = emial
        

##  --- class for contact management

class Contactmanger:
    def __init__(self):
        self.Contacts = []
        
    
    # ---- function to add new contact
    def add_contact(self,contact):
        self.Contacts.append(contact)
    # --- end 
    
    # -- function to update the contact -- #
    
    def update_contact(self,id,name,mobile,emial):
        
        for xontact in self.contacts:
            if Contact.id == id:
                Contact.name = name
                Contact.mobile = mobile
                Contact.emial = emial
                
                break
            # -- end if
        # -- end function
        
        
        
     # ---- function to delete contatct -- #########
        
    def delete_contatc(self,contact_id):
         for Contact in self.contacts:
                if Contact.id == contact_id:
                     self.contacts.remove(contact_id);
                     break
                     # -- end if 
             # -- end for loop
        # ---- end function
        
        
        ## -- function to get contact -----##
        
    def get_contact(self,contact_id):
        for contact in self.Contacts:
            if contact.id == contact_id:
                print(f"id : {contact.id} name : {contact.name} mobile : {contact.mobile} Emial : {contact.emial}")
                # -- end if
                # --- end for 
            else:
                print("none")
           
        # ---- end function
        
        
        # --- function search
        
        ## -- function searche contcat
        
    def search_contact(self,keyword):
        result = []
        for Contact in self.Contacts:
            if keyword.lower() == Contact.name.lower():
                result.append(Contact) ## -- end if
                ## -- end for
        return result;   ## -- end function
        
           
        ## -- function to save the contact to json file
        
    def save_contacts_to_file(self,filename):
        contacts_list = []
        for contact in self.Contacts:
            contact_data ={
                'id':contact.id,
                'name':contact.name,
                'mobile':contact.mobile,
                'emial': contact.emial
            }
            contacts_list.append(contact_data)
            #-- end for
            
        with open(filename,'w') as file:
            json.dump(contacts_list,file)
                
            # ---- end function
        
          
        
        ## --  function to load contact from file -- ##
    def load_contacts_from_file(self,filename):
        with open(filename,'r') as file:
            contact_list = json.load(file)
            
        for contact_data in contact_list:
            contact = Contact(contact_data['id'],contact_data['name'],contact_data['mobile'],contact_data['emial'])
            self.Contacts.append(contact)
                
             # -- end for
        ## -- end function
          
    
    
    
    
## -------------------------------- # ##

## ---------- execute the program

contact_managere = Contactmanger();

contact_one = Contact(1,"tariq",778302632,"tariq@gmail")
contact_tow = Contact(2,"Ali",778322640,"ali@gmail")

## - -- add new contatct

contact_managere.add_contact(contact_one)
contact_managere.add_contact(contact_tow)

## -- get contact to dispalay
## print(dir(Contactmanger))
contact_managere.get_contact(1)
contact_managere.get_contact(2)




     
    