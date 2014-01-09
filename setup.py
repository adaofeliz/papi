from setuptools import setup

setup(name='PAPI - Personal API',
      version='1.0',
      description='This API will guive you access to my real-time personal statistics.',
      install_requires=['Flask>=0.7.2', 'MarkupSafe', 'requests', 'requests_oauthlib','oauth2', 'pytz', 'python-dateutil'],
     )