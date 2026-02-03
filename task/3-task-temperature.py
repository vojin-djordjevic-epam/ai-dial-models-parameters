from task.app.main import run

# TODO:
#  Try the `temperature` parameter that controls the randomness of the output. It's a parameter for balancing creativity
#        and determinism. Range: 0.0 to 2.0, Default: 1.0
#  User massage: Describe the sound that the color purple makes when it's angry

run(
    deployment_name='gemini-2.5-pro',
    print_only_content=True,
    # TODO:
    #  Use `temperature` parameter with value in range from 0.0 to 1.0!
    temperature=0.8
    #  (Optional) Use `temperature` parameter with value 2.1 and check what happens
)