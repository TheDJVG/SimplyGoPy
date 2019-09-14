
SimplyGoPy: talk to transit (in Singapore)
==========================
SimplyGoPy enables you to talk to [SimplyGo](https://simplygo.transitlink.com.sg/) using Python.

Features
---------------
Currently basic features are supported:

- Login with SimplyGo login credentials.
- Retrieve notifications.
- Retrieve payment cards (you use to tap in/out at MRT/bus)
- Retrieve transactions

Authentication
------------
SimplyGo uses AES-CBC encryption when sending username and password to their API. The key/initialization vector are statically stored in `p014sg.transitlink.base.Constants` (from their Android application). 
You can encrypt your username (e-mail address) and password by running:
``` {.sourceCode .bash}
$ simplygo-encrypt mailbox@example.com
LOF3yVaERNdbNxfw1ctm63Dwqbx8ha98UR7GUEby3Pw=
```
Or use `simplygo-decrypt` to do the opposite:
``` {.sourceCode .bash}
$ simplygo-decrypt LOF3yVaERNdbNxfw1ctm63Dwqbx8ha98UR7GUEby3Pw=
mailbox@example.com
```
You can use the pre-encrypted values when starting the `simplygo` module:
``` {.sourceCode .python}
import simplygo
talk = simplygo.Ride('< encrypted username>', '<encrypted password>')
```
Installation
------------
Simple using pip:
``` {.sourceCode .bash}
$ pipenv install SimplyGoPy
🚎 🚇
```
Examples
------------
Get notifications:

``` {.sourceCode .python}
import simplygo
from pprint import pprint
rider = simplygo.Ride('<username>', '<password>')
pprint(rider.get_notifications())
```
Get card information:
``` {.sourceCode .python}
import simplygo
from pprint import pprint
rider = simplygo.Ride('<username>', '<password>')
pprint(rider.get_card_info())
```
Get user information:
``` {.sourceCode .python}
import simplygo
from pprint import pprint
rider = simplygo.Ride('<username>', '<password>')
pprint(rider.get_card_info())
```
Get transactions of today:
``` {.sourceCode .python}
import simplygo
from pprint import pprint
rider = simplygo.Ride('<username>', '<password>')
pprint(rider.get_transactions('< UniqueCode from get_card_info() >'))
```
Get transactions from date X till today:
``` {.sourceCode .python}
import simplygo
from pprint import pprint
rider = simplygo.Ride('<username>', '<password>')
pprint(rider.get_transactions('< UniqueCode from get_card_info() >', '01-01-2019'))
```
Get transactions from date X till Y:
``` {.sourceCode .python}
import simplygo
from pprint import pprint
rider = simplygo.Ride('<username>', '<password>')
pprint(rider.get_transactions('< UniqueCode from get_card_info() >', '01-06-2019', '01-07-2019'))
```
Get all transactions of this month:
``` {.sourceCode .python}
import simplygo
from pprint import pprint
rider = simplygo.Ride('<username>', '<password>')
pprint(rider.get_transactions_this_month())
```
Get transactions of this month for specific card:
``` {.sourceCode .python}
import simplygo
from pprint import pprint
rider = simplygo.Ride('<username>', '<password>')
pprint(rider.get_transactions_this_month('< UniqueCode from get_card_info() >'))
```

Disclaimer
------------
I'm in no way affiliated with SimplyGo, Transit Link, or LTA.

```
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
