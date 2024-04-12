import subprocess
import paramiko
import time

filename = 'output' + str(time.time()) + '.mp4'
print(filename)

# Run ffmpeg command to capture video and audio
ffmpeg_cmd = [
    "ffmpeg", "-f", "dshow",
    "-i", "video=Integrated Camera:audio=Microphone Array (Intel® Smart Sound Technology (Intel® SST))",
    "-vf", "format=yuv420p", "-t", "00:00:30", filename
]
subprocess.run(ffmpeg_cmd)

# SSH file transfer
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('alexpb.com', username='root', password='#T1oductdeta123;')

sftp = ssh.open_sftp()

sftp.put(filename, '/var/www/videos/' + filename)
sftp.close()

print("File uploaded successfully.")

# Close SSH connection
ssh.close()
