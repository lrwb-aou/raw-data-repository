import clock

from model.base import Base
from model.utils import UTCDateTime
from sqlalchemy import Column, Integer, Date, String

class MetricsEnrollmentStatusCache(Base):
  """Contains enrollment status metrics data grouped by HPO ID and date.
  """
  __tablename__ = 'metrics_enrollment_status_cache'
  dateInserted = Column('date_inserted', UTCDateTime, default=clock.CLOCK.now,
                        nullable=False, primary_key=True)
  hpoId = Column('hpo_id', String(20), primary_key=True)
  hpoName = Column('hpo_name', String(255), primary_key=True)
  date = Column('date', Date, nullable=False, primary_key=True)
  registeredCount = Column('registered_count', Integer, nullable=False)
  consentedCount = Column('consented_count', Integer, nullable=False)
  coreCount = Column('core_count', Integer, nullable=False)

class MetricsRaceCache(Base):
  """Contains race metrics data grouped by HPO ID and date.
  """
  __tablename__ = 'metrics_race_cache'
  dateInserted = Column('date_inserted', UTCDateTime, default=clock.CLOCK.now,
                        nullable=False, primary_key=True)
  hpoId = Column('hpo_id', String(20), primary_key=True)
  hpoName = Column('hpo_name', String(255), primary_key=True)
  date = Column('date', Date, nullable=False, primary_key=True)
  americanIndianAlaskaNative = Column('american_indian_alaska_native', Integer, nullable=False)
  asian = Column('asian', Integer, nullable=False)
  blackAfricanAmerican = Column('black_african_american', Integer, nullable=False)
  middleEasternNorthAfrican = Column('middle_eastern_north_african', Integer, nullable=False)
  nativeHawaiianOtherPacificIslander = Column('native_hawaiian_other_pacific_islander', Integer,
                                              nullable=False)
  white = Column('white', Integer, nullable=False)
  hispanicLatinoSpanish = Column('hispanic_latino_spanish', Integer, nullable=False)
  noneOfTheseFullyDescribeMe = Column('none_of_these_fully_describe_me', Integer, nullable=False)
  preferNotToAnswer = Column('prefer_not_to_answer', Integer, nullable=False)
  multiAncestry = Column('multi_ancestry', Integer, nullable=False)
  noAncestryChecked = Column('no_ancestry_checked', Integer, nullable=False)

class MetricsGenderCache(Base):
  """Contains gender metrics data grouped by HPO ID and date.
  """
  __tablename__ = 'metrics_gender_cache'
  dateInserted = Column('date_inserted', UTCDateTime, default=clock.CLOCK.now,
                        nullable=False, primary_key=True)
  hpoId = Column('hpo_id', String(20), primary_key=True)
  hpoName = Column('hpo_name', String(255), primary_key=True)
  date = Column('date', Date, nullable=False, primary_key=True)
  genderName = Column('gender_name', String(255), primary_key=True)
  genderCount = Column('gender_count', Integer, nullable=False)

class MetricsAgeCache(Base):
  """Contains age range metrics data grouped by HPO ID and date.
  """
  __tablename__ = 'metrics_age_cache'
  dateInserted = Column('date_inserted', UTCDateTime, default=clock.CLOCK.now,
                        nullable=False, primary_key=True)
  hpoId = Column('hpo_id', String(20), primary_key=True)
  hpoName = Column('hpo_name', String(255), primary_key=True)
  date = Column('date', Date, nullable=False, primary_key=True)
  ageRange = Column('age_range', String(255), primary_key=True)
  ageCount = Column('age_count', Integer, nullable=False)

class MetricsRegionCache(Base):
  """Contains region metrics data grouped by HPO and date.
  """
  __tablename__ = 'metrics_region_cache'
  dateInserted = Column('date_inserted', UTCDateTime, default=clock.CLOCK.now,
                        nullable=False, primary_key=True)
  hpoId = Column('hpo_id', String(20), primary_key=True)
  hpoName = Column('hpo_name', String(255), primary_key=True)
  date = Column('date', Date, nullable=False, primary_key=True)
  stateName = Column('state_name', String(255), primary_key=True)
  stateCount = Column('state_count', Integer, nullable=False)

class MetricsLifecycleCache(Base):
  """Contains lifecycle metrics data grouped by HPO and date.
    """
  __tablename__ = 'metrics_lifecycle_cache'
  dateInserted = Column('date_inserted', UTCDateTime, default=clock.CLOCK.now,
                        nullable=False, primary_key=True)
  hpoId = Column('hpo_id', String(20), primary_key=True)
  hpoName = Column('hpo_name', String(255), primary_key=True)
  date = Column('date', Date, nullable=False, primary_key=True)
  registered = Column('registered', Integer, nullable=False)
  consentEnrollment = Column('consent_enrollment', Integer, nullable=False)
  consentComplete = Column('consent_complete', Integer, nullable=False)
  ppiBasics = Column('ppi_basics', Integer, nullable=False)
  ppiOverallHealth = Column('ppi_overall_health', Integer, nullable=False)
  ppiLifestyle = Column('ppi_lifestyle', Integer, nullable=False)
  ppiBaselineComplete = Column('ppi_baseline_complete', Integer, nullable=False)
  physicalMeasurement = Column('physical_measurement', Integer, nullable=False)
  sampleReceived = Column('sample_received', Integer, nullable=False)
  fullParticipant = Column('full_participant', Integer, nullable=False)
