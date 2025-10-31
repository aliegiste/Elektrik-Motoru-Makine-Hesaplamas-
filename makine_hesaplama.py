import math
import matplotlib.pyplot as plt

def torque_from_power(power_w, rpm):
    """Güç (W) ve devir (rpm) biliniyorsa tork (Nm) hesaplanır."""
    return (60 * power_w) / (2 * math.pi * rpm)

def current_dc(power_w, voltage_v, efficiency=0.9):
    """DC motor akımı: I = P / (V * η)"""
    return power_w / (voltage_v * efficiency)

def current_3phase_ac(power_w, line_voltage_v, power_factor=0.9, efficiency=0.9):
    """Üç fazlı motor akımı: I = P / (√3 * V * PF * η)"""
    return power_w / (math.sqrt(3) * line_voltage_v * power_factor * efficiency)

def required_motor_power(load_power_w, safety_factor=1.25):
    """Yüke göre gerekli motor gücü"""
    return load_power_w * safety_factor

def main():
    print("=== ELEKTRİK MOTORU HESAPLAMA PROGRAMI ===")
    motor_type = input("Motor tipi (DC / AC): ").strip().upper()
    voltage = float(input("Gerilim (Volt): "))
    power_w = float(input("Güç (Watt): "))
    rpm = float(input("Devir (rpm): "))
    efficiency = float(input("Verim (örn. 0.9): "))
    safety_factor = float(input("Güvenlik faktörü (örn. 1.25): "))

    # Tork hesabı
    torque = torque_from_power(power_w, rpm)

    # Akım hesabı
    if motor_type == "DC":
        current = current_dc(power_w, voltage, efficiency)
    else:
        pf = float(input("Güç katsayısı (örn. 0.9): "))
        current = current_3phase_ac(power_w, voltage, pf, efficiency)

    # Gerekli motor gücü
    req_power = required_motor_power(power_w, safety_factor)

    print("\n=== SONUÇLAR ===")
    print(f"Tork (Nm): {torque:.3f}")
    print(f"Tahmini Akım (A): {current:.3f}")
    print(f"Gerekli Motor Gücü (W): {req_power:.1f}")

    # Tork-hız grafiği
    rpms = range(100, int(rpm * 2), 100)
    torques = [torque_from_power(power_w, n) for n in rpms]

    plt.figure(figsize=(8,5))
    plt.plot(rpms, torques)
    plt.title(f"Tork - Hız Eğrisi ({power_w} W motor)")
    plt.xlabel("Devir (rpm)")
    plt.ylabel("Tork (Nm)")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
