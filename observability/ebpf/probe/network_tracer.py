from bcc import BPF

program = """
int trace_connect(struct pt_regs *ctx) {
    bpf_trace_printk("TCP connection detected\\n");
    return 0;
}
"""

b = BPF(text=program)
b.attach_kprobe(event="tcp_connect", fn_name="trace_connect")

print("Tracing network connections...")

while True:
    print(b.trace_readline())o

