# using boto example

## Getting Started

After you clone this, in the command line you may need to go into this folder, and run

```python
python3 -m pip install boto3
```

I also made sure AWS CLI was setup with the DEFAULT as the AWS account that I was interested in exploring, in my root .aws folder.

## Output Files

Output files are put into the Results folder.

## Running the programs

### EC2 Descriptions

To get EC2 descriptions output to a json file, run this in the command line:

``` python
 python ./get_ec2_descriptions.py
 ```

The above may need to be python3 on some macs instead of python

### Examples of Boto in Console

To see other examples with console output, run this in the command line.

```python
python ./get_boto_examples.py
```
