import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Card, CardContent } from "@/components/ui/card";
import { Tabs, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { motion } from "framer-motion";

export default function SEOTool() {
  const [domain, setDomain] = useState("");
  const [tool, setTool] = useState("traffic");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleRunTool = async () => {
    if (!domain) return;
    setLoading(true);
    // Dummy simulate
    setTimeout(() => {
      setResult(`Đã chạy tool '${tool}' cho domain: ${domain}`);
      setLoading(false);
    }, 1500);
  };

  return (
    <main className="min-h-screen bg-gray-100 p-4 flex flex-col items-center">
      <motion.h1
        initial={{ y: -20, opacity: 0 }}
        animate={{ y: 0, opacity: 1 }}
        transition={{ duration: 0.4 }}
        className="text-3xl font-bold mb-6 text-center"
      >
        🔍 SEO Intelligence Tool
      </motion.h1>

      <Card className="w-full max-w-xl p-6 shadow-xl">
        <CardContent className="flex flex-col gap-4">
          <Input
            placeholder="Nhập domain hoặc từ khoá..."
            value={domain}
            onChange={(e) => setDomain(e.target.value)}
          />

          <Tabs defaultValue="traffic" className="w-full">
            <TabsList className="w-full grid grid-cols-2">
              <TabsTrigger value="traffic" onClick={() => setTool("traffic")}>So sánh traffic</TabsTrigger>
              <TabsTrigger value="keyword" onClick={() => setTool("keyword")}>Gợi ý từ khoá</TabsTrigger>
            </TabsList>
          </Tabs>

          <Button onClick={handleRunTool} disabled={loading} className="mt-2">
            {loading ? "Đang xử lý..." : "Chạy tool"}
          </Button>

          {result && (
            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              transition={{ delay: 0.2 }}
              className="bg-green-100 text-green-800 rounded-lg p-4 mt-4"
            >
              {result}
            </motion.div>
          )}
        </CardContent>
      </Card>
    </main>
  );
}
