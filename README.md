# This is completing a test task for the Springs company.

It's a web application where the user can upload a PDF file 
and get answers to questions about the uploaded document on a separate page.


## Run project:

Go to the folder with main.py file
install requirement project's packages:

```
pip install -r requirements.txt
```
in main.py write your OPENAI_API_KEY in ``` os.environ['OPENAI_API_KEY'] = ""  ```
then run the program:
```
flask --app main run
```

the web application will be running on http://127.0.0.1:5000

## Run project with Docker:
Build the image:
```
docker image build --tag 'test_task' .
```
Run the image:
```
docker run image_name
```
P.S.:There may be problems with hosts. Don't know how to fix it yet. 

## stages of work:
- HTML pages (5-10 min)
- Uploading documents(20-30 min)
- Text processing(~2 hours)
- Answers to the questions(1-1.5 hours)