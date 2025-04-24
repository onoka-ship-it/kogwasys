// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract VulnerableContract {
    address public priceFeed;
    mapping(address => uint) public balances;

    function deposit() public payable {
        balances[msg.sender] += msg.value;
    }

    function withdraw() public {
        require(balances[msg.sender] > 0);
        (bool success, ) = msg.sender.call{value: balances[msg.sender]}("");
        require(success, "Withdraw failed");
        balances[msg.sender] = 0;
    }

    function getPrice() public view returns (uint) {
        return uint(blockhash(block.number - 1));
    }
}
