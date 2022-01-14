# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class HippoCadre(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    parent = models.CharField(max_length=255, blank=True, null=True)
    last_modified = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    remap = models.CharField(max_length=255, blank=True, null=True)
    i2ce_hidden = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    cadre_dhis_uid = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hippo_cadre'


class HippoEthnicity(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    parent = models.CharField(max_length=255, blank=True, null=True)
    last_modified = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    remap = models.CharField(max_length=255, blank=True, null=True)
    i2ce_hidden = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hippo_ethnicity'


class HippoFacility(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    parent = models.CharField(max_length=255, blank=True, null=True)
    last_modified = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    remap = models.CharField(max_length=255, blank=True, null=True)
    i2ce_hidden = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    csd_uuid = models.CharField(max_length=255, blank=True, null=True)
    facility_category = models.CharField(max_length=255, blank=True, null=True)
    facility_dhis_uuid = models.CharField(max_length=255, blank=True, null=True)
    facility_level = models.CharField(max_length=255, blank=True, null=True)
    facility_owner = models.CharField(max_length=255, blank=True, null=True)
    facility_service = models.CharField(max_length=255, blank=True, null=True)
    facility_status = models.CharField(max_length=255, blank=True, null=True)
    facility_type = models.CharField(max_length=255, blank=True, null=True)
    fac_code = models.CharField(max_length=255, blank=True, null=True)
    hmis_code = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.CharField(max_length=255, blank=True, null=True)
    longitude = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hippo_facility'


class ZebraAllStaff(models.Model):
    last_modified = models.DateTimeField(blank=True, null=True)
    primary_form_id = models.CharField(db_column='primary_form+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    primary_form_parent = models.CharField(db_column='primary_form+parent', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    primary_form_position = models.CharField(db_column='primary_form+position', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    primary_form_end_date = models.DateTimeField(db_column='primary_form+end_date', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    primary_form_reason = models.CharField(db_column='primary_form+reason', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    primary_form_start_date = models.DateTimeField(db_column='primary_form+start_date', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    position_id = models.CharField(db_column='position+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    position_parent = models.CharField(db_column='position+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    position_facility = models.CharField(db_column='position+facility', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    position_job = models.CharField(db_column='position+job', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    position_department = models.CharField(db_column='position+department', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    position_paystation = models.CharField(db_column='position+paystation', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    position_ministry = models.CharField(db_column='position+ministry', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    position_pos_type = models.CharField(db_column='position+pos_type', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    start_salary_id = models.CharField(db_column='start_salary+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    start_salary_parent = models.CharField(db_column='start_salary+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    person_id = models.CharField(db_column='person+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    person_parent = models.CharField(db_column='person+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    person_nationality = models.CharField(db_column='person+nationality', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    person_disability_type = models.CharField(db_column='person+disability_type', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    person_firstname = models.CharField(db_column='person+firstname', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    person_name_title = models.CharField(db_column='person+name_title', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    person_othername = models.CharField(db_column='person+othername', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    person_residence = models.CharField(db_column='person+residence', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    person_surname = models.CharField(db_column='person+surname', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    current_salary_id = models.CharField(db_column='current_salary+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    current_salary_parent = models.CharField(db_column='current_salary+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    facility_id = models.CharField(db_column='facility+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    facility_parent = models.CharField(db_column='facility+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    facility_location = models.CharField(db_column='facility+location', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    facility_facility_category = models.CharField(db_column='facility+facility_category', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    facility_facility_level = models.CharField(db_column='facility+facility_level', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    facility_facility_type = models.CharField(db_column='facility+facility_type', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    facility_fac_code = models.CharField(db_column='facility+fac_code', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    facility_name = models.CharField(db_column='facility+name', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    job_id = models.CharField(db_column='job+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    job_parent = models.CharField(db_column='job+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    job_classification = models.CharField(db_column='job+classification', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    job_job_sub_category = models.CharField(db_column='job+job_sub_category', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    job_cadre = models.CharField(db_column='job+cadre', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    job_title = models.CharField(db_column='job+title', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    department_id = models.CharField(db_column='department+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    department_parent = models.CharField(db_column='department+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    paystation_id = models.CharField(db_column='paystation+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    paystation_parent = models.CharField(db_column='paystation+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    paystation_location = models.CharField(db_column='paystation+location', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    demographic_id = models.CharField(db_column='demographic+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    demographic_parent = models.CharField(db_column='demographic+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    demographic_birth_date = models.DateTimeField(db_column='demographic+birth_date', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    demographic_ethnicity = models.TextField(db_column='demographic+ethnicity', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    demographic_gender = models.TextField(db_column='demographic+gender', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    emergency_id = models.CharField(db_column='emergency+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    emergency_parent = models.CharField(db_column='emergency+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    employment_id = models.CharField(db_column='employment+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    employment_parent = models.CharField(db_column='employment+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    home_id = models.CharField(db_column='home+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    home_parent = models.CharField(db_column='home+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    nationality_id = models.CharField(db_column='nationality+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    nationality_parent = models.CharField(db_column='nationality+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    national_id_no_id = models.CharField(db_column='national_id_no+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    national_id_no_parent = models.CharField(db_column='national_id_no+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    national_id_no_id_num = models.CharField(db_column='national_id_no+id_num', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    national_id_no_id_type = models.CharField(db_column='national_id_no+id_type', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    nssf_no_id = models.CharField(db_column='NSSF_No+id', max_length=48, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nssf_no_parent = models.CharField(db_column='NSSF_No+parent', max_length=48, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nssf_no_id_type = models.CharField(db_column='NSSF_No+id_type', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    personal_no_id = models.CharField(db_column='personal_no+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    personal_no_parent = models.CharField(db_column='personal_no+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    personal_no_id_num = models.CharField(db_column='personal_no+id_num', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    personal_no_id_type = models.CharField(db_column='personal_no+id_type', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    person_contact_personal_id = models.CharField(db_column='person_contact_personal+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    person_contact_personal_parent = models.CharField(db_column='person_contact_personal+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    person_contact_personal_email = models.TextField(db_column='person_contact_personal+email', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    person_contact_personal_mobile_phone = models.TextField(db_column='person_contact_personal+mobile_phone', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    work_id = models.CharField(db_column='work+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    work_parent = models.CharField(db_column='work+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    facility_county_id = models.CharField(db_column='facility_county+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    facility_county_parent = models.CharField(db_column='facility_county+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    facility_county_name = models.TextField(db_column='facility_county+name', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    classification_id = models.CharField(db_column='classification+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    classification_parent = models.CharField(db_column='classification+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    job_sub_category_id = models.CharField(db_column='job_sub_category+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    job_sub_category_parent = models.CharField(db_column='job_sub_category+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    job_sub_category_cadre = models.CharField(db_column='job_sub_category+cadre', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    county_id = models.CharField(db_column='county+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    county_parent = models.CharField(db_column='county+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    county_name = models.TextField(db_column='county+name', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    cadre_id = models.CharField(db_column='cadre+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    cadre_parent = models.CharField(db_column='cadre+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    pay_district_id = models.CharField(db_column='pay_district+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    pay_district_parent = models.CharField(db_column='pay_district+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    last_md5 = models.CharField(unique=True, max_length=16, blank=True, null=True)
    md5 = models.CharField(unique=True, max_length=16, blank=True, null=True)
    field_facility_county = models.CharField(db_column='+facility_county', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'zebra_all_staff'


class ZebraCurrentStaff(models.Model):
    last_modified = models.DateTimeField(blank=True, null=True)
    primary_form_id = models.CharField(db_column='primary_form+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    primary_form_parent = models.CharField(db_column='primary_form+parent', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    primary_form_position = models.CharField(db_column='primary_form+position', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    primary_form_start_date = models.DateTimeField(db_column='primary_form+start_date', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    primary_form_end_date = models.DateTimeField(db_column='primary_form+end_date', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    current_salary_id = models.CharField(db_column='current_salary+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    current_salary_parent = models.CharField(db_column='current_salary+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    current_salary_end_date = models.DateTimeField(db_column='current_salary+end_date', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    person_id = models.CharField(db_column='person+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    person_parent = models.CharField(db_column='person+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    person_nationality = models.CharField(db_column='person+nationality', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    person_disability_type = models.CharField(db_column='person+disability_type', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    person_firstname = models.CharField(db_column='person+firstname', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    person_name_title = models.CharField(db_column='person+name_title', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    person_othername = models.CharField(db_column='person+othername', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    person_residence = models.CharField(db_column='person+residence', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    person_surname = models.CharField(db_column='person+surname', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    position_id = models.CharField(db_column='position+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    position_parent = models.CharField(db_column='position+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    position_department = models.CharField(db_column='position+department', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    position_job = models.CharField(db_column='position+job', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    position_facility = models.CharField(db_column='position+facility', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    position_hiv_program_time = models.CharField(db_column='position+hiv_program_time', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    position_ministry = models.CharField(db_column='position+ministry', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    position_pos_type = models.CharField(db_column='position+pos_type', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    start_salary_id = models.CharField(db_column='start_salary+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    start_salary_parent = models.CharField(db_column='start_salary+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    start_salary_start_date = models.DateTimeField(db_column='start_salary+start_date', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    demographic_id = models.CharField(db_column='demographic+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    demographic_parent = models.CharField(db_column='demographic+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    demographic_birth_date = models.DateTimeField(db_column='demographic+birth_date', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    demographic_ethnicity = models.TextField(db_column='demographic+ethnicity', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    demographic_gender = models.TextField(db_column='demographic+gender', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    emergency_id = models.CharField(db_column='emergency+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    emergency_parent = models.CharField(db_column='emergency+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    employment_id = models.CharField(db_column='employment+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    employment_parent = models.CharField(db_column='employment+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    employment_start_date = models.DateTimeField(db_column='employment+start_date', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    home_id = models.CharField(db_column='home+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    home_parent = models.CharField(db_column='home+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    home_email = models.TextField(db_column='home+email', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    home_telephone = models.TextField(db_column='home+telephone', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    nationality_id = models.CharField(db_column='nationality+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    nationality_parent = models.CharField(db_column='nationality+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    national_id_no_id = models.CharField(db_column='national_id_no+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    national_id_no_parent = models.CharField(db_column='national_id_no+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    national_id_no_id_num = models.CharField(db_column='national_id_no+id_num', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    national_id_no_id_type = models.CharField(db_column='national_id_no+id_type', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    nssf_no_id = models.CharField(db_column='NSSF_No+id', max_length=48, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nssf_no_parent = models.CharField(db_column='NSSF_No+parent', max_length=48, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nssf_no_id_type = models.CharField(db_column='NSSF_No+id_type', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    personal_no_id = models.CharField(db_column='personal_no+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    personal_no_parent = models.CharField(db_column='personal_no+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    personal_no_id_num = models.CharField(db_column='personal_no+id_num', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    personal_no_id_type = models.CharField(db_column='personal_no+id_type', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    person_contact_personal_id = models.CharField(db_column='person_contact_personal+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    person_contact_personal_parent = models.CharField(db_column='person_contact_personal+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    person_specialty_id = models.CharField(db_column='person_specialty+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    person_specialty_parent = models.CharField(db_column='person_specialty+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    person_specialty_specialty = models.TextField(db_column='person_specialty+specialty', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    registration_id = models.CharField(db_column='registration+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    registration_parent = models.CharField(db_column='registration+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    registration_registration_number = models.TextField(db_column='registration+registration_number', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    registration_license_expiration = models.DateTimeField(db_column='registration+license_expiration', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    registration_license_number = models.TextField(db_column='registration+license_number', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    work_id = models.CharField(db_column='work+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    work_parent = models.CharField(db_column='work+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    department_id = models.CharField(db_column='department+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    department_parent = models.CharField(db_column='department+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    department_division = models.TextField(db_column='department+division', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    department_name = models.TextField(db_column='department+name', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    job_id = models.CharField(db_column='job+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    job_parent = models.CharField(db_column='job+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    job_job_sub_category = models.CharField(db_column='job+job_sub_category', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    job_cadre = models.CharField(db_column='job+cadre', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    job_classification = models.CharField(db_column='job+classification', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    job_salary_grade = models.CharField(db_column='job+salary_grade', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    facility_id = models.CharField(db_column='facility+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    facility_parent = models.CharField(db_column='facility+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    facility_location = models.CharField(db_column='facility+location', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    facility_facility_level = models.CharField(db_column='facility+facility_level', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    facility_facility_type = models.CharField(db_column='facility+facility_type', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    facility_fac_code = models.CharField(db_column='facility+fac_code', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    facility_name = models.CharField(db_column='facility+name', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    job_sub_category_id = models.CharField(db_column='job_sub_category+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    job_sub_category_parent = models.CharField(db_column='job_sub_category+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    job_sub_category_cadre = models.TextField(db_column='job_sub_category+cadre', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    job_sub_category_code = models.TextField(db_column='job_sub_category+code', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    job_sub_category_name = models.TextField(db_column='job_sub_category+name', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    cadre_id = models.CharField(db_column='cadre+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    cadre_parent = models.CharField(db_column='cadre+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    cadre_name = models.TextField(db_column='cadre+name', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    classification_id = models.CharField(db_column='classification+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    classification_parent = models.CharField(db_column='classification+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_id = models.CharField(db_column='ward+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_parent = models.CharField(db_column='ward+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_constituency = models.CharField(db_column='ward+constituency', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_name = models.CharField(db_column='ward+name', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    constituency_id = models.CharField(db_column='constituency+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    constituency_parent = models.CharField(db_column='constituency+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    constituency_county = models.CharField(db_column='constituency+county', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    constituency_name = models.CharField(db_column='constituency+name', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    county_id = models.CharField(db_column='county+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    county_parent = models.CharField(db_column='county+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    county_district = models.CharField(db_column='county+district', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    county_name = models.CharField(db_column='county+name', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    facility_county_id = models.CharField(db_column='facility_county+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    facility_county_parent = models.CharField(db_column='facility_county+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    facility_county_name = models.TextField(db_column='facility_county+name', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_constituency_id = models.CharField(db_column='ward_constituency+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_constituency_parent = models.CharField(db_column='ward_constituency+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_constituency_county = models.CharField(db_column='ward_constituency+county', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_constituency_name = models.CharField(db_column='ward_constituency+name', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    constituency_county_id = models.CharField(db_column='constituency_county+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    constituency_county_parent = models.CharField(db_column='constituency_county+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    constituency_county_district = models.CharField(db_column='constituency_county+district', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    constituency_county_name = models.CharField(db_column='constituency_county+name', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    county_district_id = models.CharField(db_column='county_district+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    county_district_parent = models.CharField(db_column='county_district+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    county_district_name = models.TextField(db_column='county_district+name', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_county_id = models.CharField(db_column='ward_county+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_county_parent = models.CharField(db_column='ward_county+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_county_district = models.CharField(db_column='ward_county+district', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_county_name = models.CharField(db_column='ward_county+name', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    constituency_district_id = models.CharField(db_column='constituency_district+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    constituency_district_parent = models.CharField(db_column='constituency_district+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    constituency_district_name = models.TextField(db_column='constituency_district+name', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_district_id = models.CharField(db_column='ward_district+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_district_parent = models.CharField(db_column='ward_district+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_district_name = models.TextField(db_column='ward_district+name', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    last_md5 = models.CharField(unique=True, max_length=16, blank=True, null=True)
    md5 = models.CharField(unique=True, max_length=16, blank=True, null=True)
    field_age_group = models.CharField(db_column='+age_group', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_currentage = models.CharField(db_column='+CurrentAge', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_current_staff_constituency = models.CharField(db_column='+current_staff_constituency', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_current_staff_county = models.CharField(db_column='+current_staff_county', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_current_staff_sub_county = models.CharField(db_column='+current_staff_sub_county', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_facility_county = models.CharField(db_column='+facility_county', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_hire_year = models.IntegerField(db_column='+hire_year', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_registration_status = models.CharField(db_column='+registration_status', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_retirement_date = models.DateTimeField(db_column='+retirement_date', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_staff_hiv_program_time = models.CharField(db_column='+Staff_HIV_Program_time', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'zebra_current_staff'


class ZebraCurrentStaffChews(models.Model):
    last_modified = models.DateTimeField(blank=True, null=True)
    primary_form_id = models.CharField(db_column='primary_form+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    primary_form_parent = models.CharField(db_column='primary_form+parent', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    primary_form_position = models.CharField(db_column='primary_form+position', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    primary_form_end_date = models.DateTimeField(db_column='primary_form+end_date', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    person_id = models.CharField(db_column='person+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    person_parent = models.CharField(db_column='person+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    person_nationality = models.CharField(db_column='person+nationality', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    person_disability_type = models.CharField(db_column='person+disability_type', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    person_firstname = models.CharField(db_column='person+firstname', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    person_name_title = models.CharField(db_column='person+name_title', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    person_othername = models.CharField(db_column='person+othername', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    person_residence = models.CharField(db_column='person+residence', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    person_surname = models.CharField(db_column='person+surname', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    start_salary_id = models.CharField(db_column='start_salary+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    start_salary_parent = models.CharField(db_column='start_salary+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    start_salary_start_date = models.DateTimeField(db_column='start_salary+start_date', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    position_id = models.CharField(db_column='position+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    position_parent = models.CharField(db_column='position+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    position_facility = models.CharField(db_column='position+facility', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    position_department = models.CharField(db_column='position+department', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    position_job = models.CharField(db_column='position+job', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    position_hiv_program_time = models.CharField(db_column='position+hiv_program_time', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    position_ministry = models.CharField(db_column='position+ministry', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    position_pos_type = models.CharField(db_column='position+pos_type', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    current_salary_id = models.CharField(db_column='current_salary+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    current_salary_parent = models.CharField(db_column='current_salary+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    current_salary_end_date = models.DateTimeField(db_column='current_salary+end_date', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    demographic_id = models.CharField(db_column='demographic+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    demographic_parent = models.CharField(db_column='demographic+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    demographic_birth_date = models.DateTimeField(db_column='demographic+birth_date', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    demographic_ethnicity = models.TextField(db_column='demographic+ethnicity', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    demographic_gender = models.TextField(db_column='demographic+gender', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    emergency_id = models.CharField(db_column='emergency+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    emergency_parent = models.CharField(db_column='emergency+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    employment_id = models.CharField(db_column='employment+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    employment_parent = models.CharField(db_column='employment+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    employment_start_date = models.DateTimeField(db_column='employment+start_date', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    home_id = models.CharField(db_column='home+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    home_parent = models.CharField(db_column='home+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    nationality_id = models.CharField(db_column='nationality+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    nationality_parent = models.CharField(db_column='nationality+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    national_id_no_id = models.CharField(db_column='national_id_no+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    national_id_no_parent = models.CharField(db_column='national_id_no+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    national_id_no_id_num = models.CharField(db_column='national_id_no+id_num', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    national_id_no_id_type = models.CharField(db_column='national_id_no+id_type', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    nssf_no_id = models.CharField(db_column='NSSF_No+id', max_length=48, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nssf_no_parent = models.CharField(db_column='NSSF_No+parent', max_length=48, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nssf_no_id_type = models.CharField(db_column='NSSF_No+id_type', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    personal_no_id = models.CharField(db_column='personal_no+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    personal_no_parent = models.CharField(db_column='personal_no+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    personal_no_id_num = models.CharField(db_column='personal_no+id_num', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    personal_no_id_type = models.CharField(db_column='personal_no+id_type', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    person_contact_personal_id = models.CharField(db_column='person_contact_personal+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    person_contact_personal_parent = models.CharField(db_column='person_contact_personal+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    work_id = models.CharField(db_column='work+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    work_parent = models.CharField(db_column='work+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    facility_id = models.CharField(db_column='facility+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    facility_parent = models.CharField(db_column='facility+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    facility_location = models.CharField(db_column='facility+location', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    facility_facility_level = models.CharField(db_column='facility+facility_level', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    facility_facility_type = models.CharField(db_column='facility+facility_type', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    facility_fac_code = models.CharField(db_column='facility+fac_code', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    facility_name = models.CharField(db_column='facility+name', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    department_id = models.CharField(db_column='department+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    department_parent = models.CharField(db_column='department+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    department_division = models.TextField(db_column='department+division', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    department_name = models.TextField(db_column='department+name', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    job_id = models.CharField(db_column='job+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    job_parent = models.CharField(db_column='job+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    job_job_sub_category = models.CharField(db_column='job+job_sub_category', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    job_classification = models.CharField(db_column='job+classification', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    job_cadre = models.CharField(db_column='job+cadre', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    job_salary_grade = models.CharField(db_column='job+salary_grade', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    facility_county_id = models.CharField(db_column='facility_county+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    facility_county_parent = models.CharField(db_column='facility_county+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    facility_county_name = models.TextField(db_column='facility_county+name', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    county_id = models.CharField(db_column='county+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    county_parent = models.CharField(db_column='county+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    county_district = models.CharField(db_column='county+district', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    county_name = models.CharField(db_column='county+name', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_id = models.CharField(db_column='ward+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_parent = models.CharField(db_column='ward+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_constituency = models.CharField(db_column='ward+constituency', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    constituency_id = models.CharField(db_column='constituency+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    constituency_parent = models.CharField(db_column='constituency+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    constituency_county = models.CharField(db_column='constituency+county', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    constituency_name = models.CharField(db_column='constituency+name', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    job_sub_category_id = models.CharField(db_column='job_sub_category+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    job_sub_category_parent = models.CharField(db_column='job_sub_category+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    job_sub_category_cadre = models.TextField(db_column='job_sub_category+cadre', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    job_sub_category_code = models.TextField(db_column='job_sub_category+code', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    job_sub_category_name = models.TextField(db_column='job_sub_category+name', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    classification_id = models.CharField(db_column='classification+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    classification_parent = models.CharField(db_column='classification+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    cadre_id = models.CharField(db_column='cadre+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    cadre_parent = models.CharField(db_column='cadre+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    cadre_name = models.CharField(db_column='cadre+name', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    county_district_id = models.CharField(db_column='county_district+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    county_district_parent = models.CharField(db_column='county_district+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    county_district_name = models.TextField(db_column='county_district+name', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_constituency_id = models.CharField(db_column='ward_constituency+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_constituency_parent = models.CharField(db_column='ward_constituency+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_constituency_county = models.CharField(db_column='ward_constituency+county', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_constituency_name = models.CharField(db_column='ward_constituency+name', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    constituency_county_id = models.CharField(db_column='constituency_county+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    constituency_county_parent = models.CharField(db_column='constituency_county+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    constituency_county_district = models.CharField(db_column='constituency_county+district', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    constituency_county_name = models.CharField(db_column='constituency_county+name', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_county_id = models.CharField(db_column='ward_county+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_county_parent = models.CharField(db_column='ward_county+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_county_district = models.CharField(db_column='ward_county+district', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_county_name = models.CharField(db_column='ward_county+name', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    constituency_district_id = models.CharField(db_column='constituency_district+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    constituency_district_parent = models.CharField(db_column='constituency_district+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    constituency_district_name = models.TextField(db_column='constituency_district+name', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_district_id = models.CharField(db_column='ward_district+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_district_parent = models.CharField(db_column='ward_district+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_district_name = models.TextField(db_column='ward_district+name', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    last_md5 = models.CharField(unique=True, max_length=16, blank=True, null=True)
    md5 = models.CharField(unique=True, max_length=16, blank=True, null=True)
    field_currentage = models.CharField(db_column='+CurrentAge', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_current_staff_constituency = models.CharField(db_column='+current_staff_constituency', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_current_staff_county = models.CharField(db_column='+current_staff_county', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_current_staff_sub_county = models.CharField(db_column='+current_staff_sub_county', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_facility_county = models.CharField(db_column='+facility_county', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_hire_year = models.IntegerField(db_column='+hire_year', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_retirement_date = models.DateTimeField(db_column='+retirement_date', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_staff_hiv_program_time = models.CharField(db_column='+Staff_HIV_Program_time', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'zebra_current_staff_chews'


class ZebraFacilityList(models.Model):
    last_modified = models.DateTimeField(blank=True, null=True)
    primary_form_id = models.CharField(db_column='primary_form+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    primary_form_parent = models.CharField(db_column='primary_form+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    primary_form_location = models.CharField(db_column='primary_form+location', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    primary_form_facility_level = models.CharField(db_column='primary_form+facility_level', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    primary_form_facility_type = models.CharField(db_column='primary_form+facility_type', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    primary_form_facility_status = models.CharField(db_column='primary_form+facility_status', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    primary_form_fac_code = models.CharField(db_column='primary_form+fac_code', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    primary_form_hmis_code = models.CharField(db_column='primary_form+hmis_code', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    primary_form_latitude = models.CharField(db_column='primary_form+latitude', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    primary_form_longitude = models.CharField(db_column='primary_form+longitude', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    primary_form_name = models.CharField(db_column='primary_form+name', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    constituency_id = models.CharField(db_column='constituency+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    constituency_parent = models.CharField(db_column='constituency+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    constituency_county = models.CharField(db_column='constituency+county', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    constituency_name = models.CharField(db_column='constituency+name', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    county_id = models.CharField(db_column='county+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    county_parent = models.CharField(db_column='county+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    county_district = models.CharField(db_column='county+district', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    county_name = models.CharField(db_column='county+name', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    district_id = models.CharField(db_column='district+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    district_parent = models.CharField(db_column='district+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    district_name = models.TextField(db_column='district+name', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    facility_contact_id = models.CharField(db_column='facility_contact+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    facility_contact_parent = models.CharField(db_column='facility_contact+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    facility_contact_address = models.TextField(db_column='facility_contact+address', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    facility_contact_telephone = models.TextField(db_column='facility_contact+telephone', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    facility_contact_email = models.TextField(db_column='facility_contact+email', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    facility_contact_notes = models.TextField(db_column='facility_contact+notes', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    facility_level_id = models.CharField(db_column='facility_level+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    facility_level_parent = models.CharField(db_column='facility_level+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    facility_level_name = models.TextField(db_column='facility_level+name', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    facility_type_id = models.CharField(db_column='facility_type+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    facility_type_parent = models.CharField(db_column='facility_type+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    facility_type_name = models.TextField(db_column='facility_type+name', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_id = models.CharField(db_column='ward+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_parent = models.CharField(db_column='ward+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_constituency = models.CharField(db_column='ward+constituency', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_name = models.CharField(db_column='ward+name', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    constituency_county_id = models.CharField(db_column='constituency_county+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    constituency_county_parent = models.CharField(db_column='constituency_county+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    constituency_county_district = models.CharField(db_column='constituency_county+district', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    constituency_county_name = models.CharField(db_column='constituency_county+name', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    county_district_id = models.CharField(db_column='county_district+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    county_district_parent = models.CharField(db_column='county_district+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    county_district_name = models.TextField(db_column='county_district+name', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_constituency_id = models.CharField(db_column='ward_constituency+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_constituency_parent = models.CharField(db_column='ward_constituency+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_constituency_county = models.CharField(db_column='ward_constituency+county', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_constituency_name = models.CharField(db_column='ward_constituency+name', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    constituency_district_id = models.CharField(db_column='constituency_district+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    constituency_district_parent = models.CharField(db_column='constituency_district+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    constituency_district_name = models.TextField(db_column='constituency_district+name', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_county_id = models.CharField(db_column='ward_county+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_county_parent = models.CharField(db_column='ward_county+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_county_district = models.CharField(db_column='ward_county+district', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_county_name = models.CharField(db_column='ward_county+name', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_district_id = models.CharField(db_column='ward_district+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_district_parent = models.CharField(db_column='ward_district+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_district_name = models.TextField(db_column='ward_district+name', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    last_md5 = models.CharField(unique=True, max_length=16, blank=True, null=True)
    md5 = models.CharField(unique=True, max_length=16, blank=True, null=True)
    field_facility_constituency = models.CharField(db_column='+Facility_Constituency', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_facilitycounty = models.CharField(db_column='+FacilityCounty', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_facilitycountyid = models.CharField(db_column='+FacilityCountyID', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_facility_sub_county = models.CharField(db_column='+Facility_Sub_County', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'zebra_facility_list'


class ZebraStaffPerCounty(models.Model):
    last_modified = models.DateTimeField(blank=True, null=True)
    primary_form_id = models.CharField(db_column='primary_form+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    primary_form_parent = models.CharField(db_column='primary_form+parent', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    primary_form_position = models.CharField(db_column='primary_form+position', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    primary_form_end_date = models.DateTimeField(db_column='primary_form+end_date', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    current_salary_id = models.CharField(db_column='current_salary+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    current_salary_parent = models.CharField(db_column='current_salary+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    current_salary_end_date = models.DateTimeField(db_column='current_salary+end_date', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    person_id = models.CharField(db_column='person+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    person_parent = models.CharField(db_column='person+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    person_nationality = models.CharField(db_column='person+nationality', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    person_firstname = models.CharField(db_column='person+firstname', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    position_id = models.CharField(db_column='position+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    position_parent = models.CharField(db_column='position+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    position_department = models.CharField(db_column='position+department', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    position_job = models.CharField(db_column='position+job', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    position_facility = models.CharField(db_column='position+facility', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    start_salary_id = models.CharField(db_column='start_salary+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    start_salary_parent = models.CharField(db_column='start_salary+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    start_salary_start_date = models.DateTimeField(db_column='start_salary+start_date', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    demographic_id = models.CharField(db_column='demographic+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    demographic_parent = models.CharField(db_column='demographic+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    emergency_id = models.CharField(db_column='emergency+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    emergency_parent = models.CharField(db_column='emergency+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    employment_id = models.CharField(db_column='employment+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    employment_parent = models.CharField(db_column='employment+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    home_id = models.CharField(db_column='home+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    home_parent = models.CharField(db_column='home+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    nationality_id = models.CharField(db_column='nationality+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    nationality_parent = models.CharField(db_column='nationality+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    national_id_no_id = models.CharField(db_column='national_id_no+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    national_id_no_parent = models.CharField(db_column='national_id_no+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    national_id_no_id_type = models.CharField(db_column='national_id_no+id_type', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    nssf_no_id = models.CharField(db_column='NSSF_No+id', max_length=48, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nssf_no_parent = models.CharField(db_column='NSSF_No+parent', max_length=48, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nssf_no_id_type = models.CharField(db_column='NSSF_No+id_type', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    personal_no_id = models.CharField(db_column='personal_no+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    personal_no_parent = models.CharField(db_column='personal_no+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    personal_no_id_type = models.CharField(db_column='personal_no+id_type', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    person_contact_personal_id = models.CharField(db_column='person_contact_personal+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    person_contact_personal_parent = models.CharField(db_column='person_contact_personal+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    person_specialty_id = models.CharField(db_column='person_specialty+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    person_specialty_parent = models.CharField(db_column='person_specialty+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    registration_id = models.CharField(db_column='registration+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    registration_parent = models.CharField(db_column='registration+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    work_id = models.CharField(db_column='work+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    work_parent = models.CharField(db_column='work+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    department_id = models.CharField(db_column='department+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    department_parent = models.CharField(db_column='department+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    job_id = models.CharField(db_column='job+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    job_parent = models.CharField(db_column='job+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    job_job_sub_category = models.CharField(db_column='job+job_sub_category', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    job_cadre = models.CharField(db_column='job+cadre', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    job_classification = models.CharField(db_column='job+classification', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    facility_id = models.CharField(db_column='facility+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    facility_parent = models.CharField(db_column='facility+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    facility_location = models.CharField(db_column='facility+location', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    job_sub_category_id = models.CharField(db_column='job_sub_category+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    job_sub_category_parent = models.CharField(db_column='job_sub_category+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    cadre_id = models.CharField(db_column='cadre+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    cadre_parent = models.CharField(db_column='cadre+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    classification_id = models.CharField(db_column='classification+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    classification_parent = models.CharField(db_column='classification+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_id = models.CharField(db_column='ward+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_parent = models.CharField(db_column='ward+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_constituency = models.CharField(db_column='ward+constituency', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    constituency_id = models.CharField(db_column='constituency+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    constituency_parent = models.CharField(db_column='constituency+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    constituency_county = models.CharField(db_column='constituency+county', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    county_id = models.CharField(db_column='county+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    county_parent = models.CharField(db_column='county+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    county_district = models.CharField(db_column='county+district', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    county_name = models.CharField(db_column='county+name', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    facility_county_id = models.CharField(db_column='facility_county+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    facility_county_parent = models.CharField(db_column='facility_county+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    facility_county_name = models.TextField(db_column='facility_county+name', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    facility_county_population = models.IntegerField(db_column='facility_county+population', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_constituency_id = models.CharField(db_column='ward_constituency+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_constituency_parent = models.CharField(db_column='ward_constituency+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_constituency_county = models.CharField(db_column='ward_constituency+county', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    constituency_county_id = models.CharField(db_column='constituency_county+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    constituency_county_parent = models.CharField(db_column='constituency_county+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    constituency_county_district = models.CharField(db_column='constituency_county+district', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    county_district_id = models.CharField(db_column='county_district+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    county_district_parent = models.CharField(db_column='county_district+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_county_id = models.CharField(db_column='ward_county+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_county_parent = models.CharField(db_column='ward_county+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_county_district = models.CharField(db_column='ward_county+district', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    constituency_district_id = models.CharField(db_column='constituency_district+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    constituency_district_parent = models.CharField(db_column='constituency_district+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_district_id = models.CharField(db_column='ward_district+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_district_parent = models.CharField(db_column='ward_district+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    last_md5 = models.CharField(unique=True, max_length=16, blank=True, null=True)
    md5 = models.CharField(unique=True, max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zebra_staff_per_county'


class ZebraStaffRegistered(models.Model):
    last_modified = models.DateTimeField(blank=True, null=True)
    primary_form_id = models.CharField(db_column='primary_form+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    primary_form_parent = models.CharField(db_column='primary_form+parent', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    primary_form_position = models.CharField(db_column='primary_form+position', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    primary_form_start_date = models.DateTimeField(db_column='primary_form+start_date', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    primary_form_end_date = models.DateTimeField(db_column='primary_form+end_date', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    person_id = models.CharField(db_column='person+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    person_parent = models.CharField(db_column='person+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    person_nationality = models.CharField(db_column='person+nationality', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    person_firstname = models.CharField(db_column='person+firstname', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    person_name_title = models.CharField(db_column='person+name_title', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    person_othername = models.CharField(db_column='person+othername', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    person_surname = models.CharField(db_column='person+surname', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    current_salary_id = models.CharField(db_column='current_salary+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    current_salary_parent = models.CharField(db_column='current_salary+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    current_salary_end_date = models.DateTimeField(db_column='current_salary+end_date', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    start_salary_id = models.CharField(db_column='start_salary+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    start_salary_parent = models.CharField(db_column='start_salary+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    start_salary_start_date = models.DateTimeField(db_column='start_salary+start_date', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    position_id = models.CharField(db_column='position+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    position_parent = models.CharField(db_column='position+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    position_department = models.CharField(db_column='position+department', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    position_paystation = models.CharField(db_column='position+paystation', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    position_facility = models.CharField(db_column='position+facility', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    position_job = models.CharField(db_column='position+job', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    position_division = models.CharField(db_column='position+division', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    position_ministry = models.CharField(db_column='position+ministry', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    demographic_id = models.CharField(db_column='demographic+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    demographic_parent = models.CharField(db_column='demographic+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    demographic_gender = models.TextField(db_column='demographic+gender', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    emergency_id = models.CharField(db_column='emergency+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    emergency_parent = models.CharField(db_column='emergency+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    employment_id = models.CharField(db_column='employment+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    employment_parent = models.CharField(db_column='employment+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    home_id = models.CharField(db_column='home+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    home_parent = models.CharField(db_column='home+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    nationality_id = models.CharField(db_column='nationality+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    nationality_parent = models.CharField(db_column='nationality+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    national_id_no_id = models.CharField(db_column='national_id_no+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    national_id_no_parent = models.CharField(db_column='national_id_no+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    national_id_no_id_num = models.CharField(db_column='national_id_no+id_num', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    national_id_no_id_type = models.CharField(db_column='national_id_no+id_type', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    nssf_no_id = models.CharField(db_column='NSSF_No+id', max_length=48, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nssf_no_parent = models.CharField(db_column='NSSF_No+parent', max_length=48, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nssf_no_id_type = models.CharField(db_column='NSSF_No+id_type', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    personal_no_id = models.CharField(db_column='personal_no+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    personal_no_parent = models.CharField(db_column='personal_no+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    personal_no_id_num = models.CharField(db_column='personal_no+id_num', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    personal_no_id_type = models.CharField(db_column='personal_no+id_type', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    person_contact_personal_id = models.CharField(db_column='person_contact_personal+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    person_contact_personal_parent = models.CharField(db_column='person_contact_personal+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    registration_id = models.CharField(db_column='registration+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    registration_parent = models.CharField(db_column='registration+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    registration_registration_number = models.CharField(db_column='registration+registration_number', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    registration_license_expiration = models.DateTimeField(db_column='registration+license_expiration', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    registration_license_number = models.CharField(db_column='registration+license_number', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    registration_council = models.CharField(db_column='registration+council', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    registration_registration_date = models.DateTimeField(db_column='registration+registration_date', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    work_id = models.CharField(db_column='work+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    work_parent = models.CharField(db_column='work+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    department_id = models.CharField(db_column='department+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    department_parent = models.CharField(db_column='department+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    paystation_id = models.CharField(db_column='paystation+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    paystation_parent = models.CharField(db_column='paystation+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    facility_id = models.CharField(db_column='facility+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    facility_parent = models.CharField(db_column='facility+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    facility_location = models.CharField(db_column='facility+location', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    facility_facility_type = models.CharField(db_column='facility+facility_type', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    job_id = models.CharField(db_column='job+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    job_parent = models.CharField(db_column='job+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    job_job_sub_category = models.CharField(db_column='job+job_sub_category', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    job_cadre = models.CharField(db_column='job+cadre', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    job_classification = models.CharField(db_column='job+classification', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_id = models.CharField(db_column='ward+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_parent = models.CharField(db_column='ward+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_constituency = models.CharField(db_column='ward+constituency', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    county_id = models.CharField(db_column='county+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    county_parent = models.CharField(db_column='county+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    county_district = models.CharField(db_column='county+district', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    county_name = models.CharField(db_column='county+name', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    facility_county_id = models.CharField(db_column='facility_county+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    facility_county_parent = models.CharField(db_column='facility_county+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    facility_county_name = models.TextField(db_column='facility_county+name', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    constituency_id = models.CharField(db_column='constituency+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    constituency_parent = models.CharField(db_column='constituency+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    constituency_county = models.CharField(db_column='constituency+county', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    job_sub_category_id = models.CharField(db_column='job_sub_category+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    job_sub_category_parent = models.CharField(db_column='job_sub_category+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    job_sub_category_cadre = models.CharField(db_column='job_sub_category+cadre', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    job_sub_category_name = models.CharField(db_column='job_sub_category+name', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    cadre_id = models.CharField(db_column='cadre+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    cadre_parent = models.CharField(db_column='cadre+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    classification_id = models.CharField(db_column='classification+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    classification_parent = models.CharField(db_column='classification+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_constituency_id = models.CharField(db_column='ward_constituency+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_constituency_parent = models.CharField(db_column='ward_constituency+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_constituency_county = models.CharField(db_column='ward_constituency+county', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    county_district_id = models.CharField(db_column='county_district+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    county_district_parent = models.CharField(db_column='county_district+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    county_district_name = models.TextField(db_column='county_district+name', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    constituency_county_id = models.CharField(db_column='constituency_county+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    constituency_county_parent = models.CharField(db_column='constituency_county+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    constituency_county_district = models.CharField(db_column='constituency_county+district', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    constituency_county_name = models.CharField(db_column='constituency_county+name', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_county_id = models.CharField(db_column='ward_county+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_county_parent = models.CharField(db_column='ward_county+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_county_district = models.CharField(db_column='ward_county+district', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_county_name = models.CharField(db_column='ward_county+name', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    constituency_district_id = models.CharField(db_column='constituency_district+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    constituency_district_parent = models.CharField(db_column='constituency_district+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    constituency_district_name = models.TextField(db_column='constituency_district+name', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_district_id = models.CharField(db_column='ward_district+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_district_parent = models.CharField(db_column='ward_district+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ward_district_name = models.TextField(db_column='ward_district+name', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    last_md5 = models.CharField(unique=True, max_length=16, blank=True, null=True)
    md5 = models.CharField(unique=True, max_length=16, blank=True, null=True)
    field_current_staff_county = models.CharField(db_column='+current_staff_county', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_current_staff_sub_county = models.CharField(db_column='+current_staff_sub_county', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_facility_county = models.CharField(db_column='+facility_county', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_registration_status = models.CharField(db_column='+registration_status', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'zebra_staff_registered'


class ZebraUsers(models.Model):
    last_modified = models.DateTimeField(blank=True, null=True)
    primary_form_id = models.CharField(db_column='primary_form+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    primary_form_parent = models.CharField(db_column='primary_form+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    primary_form_role = models.CharField(db_column='primary_form+role', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    primary_form_email = models.CharField(db_column='primary_form+email', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    primary_form_firstname = models.CharField(db_column='primary_form+firstname', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    primary_form_lastname = models.CharField(db_column='primary_form+lastname', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    primary_form_username = models.CharField(db_column='primary_form+username', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    role_id = models.CharField(db_column='role+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    role_parent = models.CharField(db_column='role+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    access_facility_id = models.CharField(db_column='access_facility+id', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    access_facility_parent = models.CharField(db_column='access_facility+parent', max_length=48, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    access_facility_location = models.TextField(db_column='access_facility+location', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    last_md5 = models.CharField(unique=True, max_length=16, blank=True, null=True)
    md5 = models.CharField(unique=True, max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zebra_users'
