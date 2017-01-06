import subprocess

def run(url_string):

    url = url_string

    quoted_url = '"' + url + '"'

    finished_url = "firefox " + quoted_url

    subprocess.Popen(finished_url, shell=True).wait()

    return(url_string)
