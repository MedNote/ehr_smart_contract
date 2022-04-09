# File: test_ehr.py #

def test_EHR(EHR, accounts):
    ehr = EHR.deploy({'from': accounts[0]})
    # create doctors
    ehr.createDoctor("Mantis", "Toboggan", accounts[1], 0x0)
    assert ehr.doctorExists(accounts[1])
    ehr.createDoctor("Greg", "House", accounts[2], 0x1)
    assert ehr.doctorExists(accounts[2])
    #doctors create patients
    ehr.createPatient("Dennis", "Reynolds", accounts[3], 0x2, {'from': accounts[1]})
    assert ehr.patientExists(accounts[3])
    ehr.createPatient("Strom", "Thurmond", accounts[4], 0x3, {'from': accounts[2]})
    assert ehr.patientExists(accounts[4])
    #doctors should have authorization to the patients they added...
    assert doctorAuthorized(accounts[1], accounts[3])
    assert doctorAuthorized(accounts[2], accounts[4])
    #...but not to other patients
    assert not doctorAuthorized(accounts[1], accounts[4])
    assert not doctorAuthorized(accounts[2], accounts[3])
    #authorized doctors can update the patient charts
    updateRecordHash
    
    
    
