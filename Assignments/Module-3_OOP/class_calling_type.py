class studinfo:
    stid=12
    stnm="Ashok"

    def getdata(self):
        print("ID:",self.stid)
        print("Name:",self.stnm)

#calling via object
"""st=studinfo()
st.getdata()
st.stid=56
st.stnm="Nirav"
st.getdata()"""

#calling via instance
studinfo().getdata()
studinfo().stid=78
studinfo().stnm="Sanket"
studinfo().getdata()