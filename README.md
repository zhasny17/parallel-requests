# parallel-requests
* On linux run the commando bellow to check execution time in seconds of some imeplmentations.
    * python asyncio implementation, pure concurrent execution, using one CPU core and one thread.
    ```SHELL
    $ time -p python async.py
    ```

    * python process implementation, pure parallel execution, using multiple CPU cores and threads.
    ```SHELL
    $ time -p python process.py
    ```

    * sequence requests implementation.
    ```SHELL
    $ time -p python sequence.py
    ```
