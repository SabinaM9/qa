# TEST ROBUSTNESS TRACKING (TRT) MICROSERVICE
This microservice is aimed to track how much reliable tests our QA engineers write.
It is intended to track all test executions and give us overall picture of test-suites
stability for each development squad. TRT has 2 endpoints.

**Endpoint 1**

Is used to store squad testing results to analyse them later.
[1] POST /addTestResult
Params:
o squad: string
o failedTests: int
o status: on of [“passed”,”failed”]

**Endpoint 2**

Returns data about tests of a given squad over period of given time.
[2] GET /testResults
Params:
o squad: string
o daysToFollow: int
Returns JSON
{ “details”: {
 ….
 “mm/dd/yyyy” : { status: ”a”, noffailrues: “x” }
 “mm/dd/yyyy” : { status: ”b”, noffailrues: “y” }
 “mm/dd/yyyy” : { status: ”c”, noffailrues: “z” }
 ….
 }
“totalDaysfailed”: “N”
“verdict”: < verdict >
“lastFailureUnfixedDays” : “M”
}
