from distutils.core import setup
setup(
  name='pytutor',
  packages=['pytutor'], # this must be the same as the name above
  version='1.0.0',
  description='An interface to run Phillip Guo\'s Python Tutor',
  author='Sumukh Sridhara',
  author_email='sumukh@berkeley.edu',
  url='https://github.com/okpy/pytutor', # use the URL to the github repo
  download_url='https://github.com/okpy/pytutor/archive/1.0.0.tar.gz',
  keywords=['tracing', 'education', 'okpy', 'tutor', 'debugger', 'python tutor'], # arbitrary keywords
  classifiers=[
    'Development Status :: 4 - Beta',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
  ],
)
