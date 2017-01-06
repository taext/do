import subprocess

def run(url_string):

    url = url_string

    quoted_url = '"' + url + '"'

    finished_url = "google-chrome " + quoted_url

    subp = subprocess.check_output(finished_url, shell=True)

    return(url_string)
