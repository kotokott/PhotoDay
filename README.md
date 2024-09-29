

# PhotoDay

A program that takes pictures when Windows starts.

You might know a guy who took pictures of himself for years and then made a timelapse)

I thought it was a cool idea, so I decided to write a mini-script in Python that takes a picture when the computer starts.

<h1>Installation</h1>

1. Download the package

2. Install requirements.txt (pip install -r requirements.txt)

3. Run PhotoDay.py. The program automatically creates a path for photos (by default "C:\PhotoDay\Collection").

4. Next, you need to add the program to the Windows Task Scheduler:

• Open the Task Scheduler

• Click "Action/Create Basic Task"

• Write the name of your task and click Next>

• Then select the desired condition (best to choose: "When the computer starts" or "When I log on") and click Next>

• Click "Start a program" and click Next>

• Enter the path to the Python.exe file in the "Program/script" field

• Enter the path to PhotoDay.py in the "Add arguments (optional)" field and click Next>

• and finally click Finish!

**You're done:^**
