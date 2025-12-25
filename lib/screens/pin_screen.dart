import 'package:flutter/material.dart';
import 'success_screen.dart';
import '../data/transaction_data.dart';
import '../models/transaction_model.dart';

class PinScreen extends StatefulWidget {
  const PinScreen({super.key});

  @override
  State<PinScreen> createState() => _PinScreenState();
}

class _PinScreenState extends State<PinScreen> {
  final TextEditingController pinController = TextEditingController();
  final String correctPin = "1234";

  bool isLoading = false;

  void verifyPin() async {
    setState(() {
      isLoading = true;
    });

    // Simulate payment processing delay
    await Future.delayed(const Duration(seconds: 2));

    setState(() {
      isLoading = false;
    });

    if (pinController.text == correctPin) {
      // ADD TRANSACTION TO DYNAMIC HISTORY
      transactionHistory.add(
        TransactionModel(
          title: "Paid",
          subtitle: "To Receiver",
          amount: "₹500",
          isDebit: true,
        ),
      );

      Navigator.pushReplacement(
        context,
        MaterialPageRoute(
          builder: (_) => const SuccessScreen(),
        ),
      );
    } else {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(
          content: Text("❌ Incorrect PIN"),
          backgroundColor: Colors.red,
        ),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Enter PIN"),
      ),
      body: Padding(
        padding: const EdgeInsets.all(24),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Text(
              "Confirm Payment",
              style: TextStyle(
                fontSize: 20,
                fontWeight: FontWeight.bold,
              ),
            ),
            const SizedBox(height: 20),

            TextField(
              controller: pinController,
              obscureText: true,
              keyboardType: TextInputType.number,
              decoration: InputDecoration(
                labelText: "4-digit PIN",
                border: OutlineInputBorder(
                  borderRadius: BorderRadius.circular(10),
                ),
              ),
            ),
            const SizedBox(height: 30),

            SizedBox(
              width: double.infinity,
              height: 48,
              child: ElevatedButton(
                onPressed: isLoading ? null : verifyPin,
                child: isLoading
                    ? const SizedBox(
                        height: 24,
                        width: 24,
                        child: CircularProgressIndicator(
                          strokeWidth: 3,
                          color: Colors.white,
                        ),
                      )
                    : const Text("Confirm"),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
