# CASCADE

This is the repository for the tool CASCADE of the paper "CASCADE: Detecting Inconsistencies between Code and Documentation using Automatic Test Generation".

## Structure
The package is sructured like this:
<pre>
CASCADE
|-- eval                    - Scripts which where only used in the paper eval and replication package (not part of the install)
|-- src                     - The root folder, the root of a module path for a CASCADE execution
|   |-- cascade             - The folder containing the CASCADE modules
|   |   |-- analysis        - All modules required for analysis, extend Analysis
|   |   |   |-- executor    - The modules required to execute and build a project, extend AnalysisExecutor
|   |   |   |   |-- builder - Builder modules, these are currently only used by JavaExecutor, extend Builder
|   |   |   |-- visualizer  - Visualizers to visualize the analysis results, extend AnalysisVisualizer
|   |   |-- extraction      - All modules that extract data for the ingestion of the pipeline, extend Extraction
|   |   |-- filters         - All modules to filter the extracted data, extend FilterFunction
|   |   |-- generation      - The Generators
|   |   |   |-- executor    - The explanations for the scripts
|   |   |   |-- code        - The code generator, extend Generator
|   |   |   |-- doc         - The doc generator, extend Generator
|   |   |   |-- test        - The test generator, extend Generator
|   |   |-- utils           - Several utility modules providing language agnostic and specific functionality
|   |-- resources           - The resource directory for all non-python components
|       |-- templates       - A folder for templates which can be copied (refer to UnittestExecutor)
|       |-- tools           - A folder containing tools which are used, currently only for Java
|-- tests                   - The tests
|-- setup.py                - The setup.py file to install CASCADE
|-- README.md               - This readme file
</pre>

## Tool usage
### run
<pre>
usage: CASCADE run [-h] -i INPUT_PATH -o OUTPUT_PATH -s SETUP_FILE [-m MODULE_PATH] [-extr EXTRACTION] [-codegen CODE_GENERATOR] [-testgen TEST_GENERATOR] [-docgen DOC_GENERATOR] [-ana ANALYSIS] [-exec EXECUTOR] [-visua VISUALIZER] [-filter FILTERS] [--debug-cli]

options:
  -h, --help            show this help message and exit
  -i INPUT_PATH, --input-path INPUT_PATH
                        The input path which will be used for extraction
  -o OUTPUT_PATH, --output-path OUTPUT_PATH
                        The output path in which results and temporary files will be stored
  -s SETUP_FILE, --setup-file SETUP_FILE
                        The path to the setup file defining the pipeline
  -m MODULE_PATH, --module-path MODULE_PATH
                        The path to the user defined modules.
  -extr EXTRACTION, --extraction EXTRACTION
                        A way to overwrite the key word arguments for the extraction.
  -codegen CODE_GENERATOR, --code-generator CODE_GENERATOR
                        A way to overwrite the key word arguments for the code generator.
  -testgen TEST_GENERATOR, --test-generator TEST_GENERATOR
                        A way to overwrite the key word arguments for the test generator.
  -docgen DOC_GENERATOR, --doc-generator DOC_GENERATOR
                        A way to overwrite the key word arguments for the doc generator.
  -ana ANALYSIS, --analysis ANALYSIS
                        A way to overwrite the key word arguments for the analysis.
  -exec EXECUTOR, --executor EXECUTOR
                        A way to overwrite the key word arguments for the executor.
  -visua VISUALIZER, --visualizer VISUALIZER
                        A way to overwrite the key word arguments for the visualizer.
  -filter FILTERS, --filters FILTERS
                        A way to overwrite the key word arguments for the filters.
  --debug-cli           Shows debug information for the CLI call.
</pre>

For MODULE_PATH the path has to point to the *src* directory as in this repository.

### build-sample
<pre>
usage: CASCADE build-sample [-h] -i INPUT_PATH -o OUTPUT_PATH -a ANALYZED_FILE -id ID -code-key CODE_KEY -tests-key TESTS_KEY

options:
  -h, --help            show this help message and exit
  -i INPUT_PATH, --input-path INPUT_PATH
                        The input path to the root of the analyzed project
  -o OUTPUT_PATH, --output-path OUTPUT_PATH
                        The output path in which results and temporary files will be stored
  -a ANALYZED_FILE, --analyzed-file ANALYZED_FILE
                        The path to the analyzed.json file containing the results
  -id ID                The id of the sample to build
  -code-key CODE_KEY    The key for the code to put in the project
  -tests-key TESTS_KEY  The key for the tests to put in the project
</pre>

## Build
To build our tool, execute

```
pip install .
```
